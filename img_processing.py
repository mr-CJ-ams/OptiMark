from PyQt5.QtWidgets import QMessageBox
import cv2
import numpy as np



def reorder(myPoints):

    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4, 1, 2), np.int32)
    add = myPoints.sum(1)
    # print(myPoints)
    # print(add)
    myPointsNew[0] = myPoints[np.argmin(add)]   # [0, 0]
    myPointsNew[3] = myPoints[np.argmax(add)]   # [w, h]
    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]  # [w, 0]
    myPointsNew[2] = myPoints[np.argmax(diff)]  # [0, h]
    # print(diff)

    return myPointsNew

def find_rect(contours):
    rectangles = []
    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
        if len(approx) == 4:
            rectangles.append(approx)

    # Sort rectangles based on area
    rectangles = sorted(rectangles, key=cv2.contourArea, reverse=True)

    return rectangles



def crop_adjusted(image, top, bottom, left, right):
    height, width = image.shape[:2]
    cropped = image[top:height-bottom, left:width-right]
    return cropped


def divide_rect_into_thirds(largestRect):
    # Split the image into two equal halves vertically
    top_half, bottom_half = np.vsplit(largestRect, 2)

    # Adjust the width to make it divisible by 3
    width = top_half.shape[1]
    width = width - (width % 3)

    # Adjust the height to make it divisible by 2
    height = top_half.shape[0]
    height = height - (height % 2)

    # Check if width and height adjustment is necessary
    if width != top_half.shape[1] or height != top_half.shape[0]:
        top_half = top_half[:height, :width]
        bottom_half = bottom_half[:height, :width]

    # Crop the top half into three equal parts horizontally
    _, top_third2, top_third3 = np.hsplit(top_half, 3)
    top_third2 = crop_adjusted(top_third2, 6, 6, 6, 6)
    top_third3 = crop_adjusted(top_third3, 6, 6, 6, 6)

    # Crop the bottom half into three equal parts horizontally
    bottom_third1, bottom_third2, bottom_third3 = np.hsplit(bottom_half, 3)
    bottom_third1 = crop_adjusted(bottom_third1, 6, 6, 6, 6)
    bottom_third2 = crop_adjusted(bottom_third2, 6, 6, 6, 6)
    bottom_third3 = crop_adjusted(bottom_third3, 6, 6, 6, 6)

    return top_third2, top_third3, bottom_third1, bottom_third2, bottom_third3


def splitBoxes(img, num_questions, num_choices, parent_widget):
    try:
        if num_questions == 25:
            t = 6
            b = 6
            l = 6
            r = 6
        if num_questions == 50:
            t = 4
            b = 8
            l = 4
            r = 5
        if num_questions == 80:
            t = 4
            b = 8
            l = 15
            r = 8

        q = num_questions // 5
        c = num_choices
        img = crop_adjusted(img, t, b, l, r)  # Crop the image before splitting

        imgshp0 = img.shape[0]
        imgshp1 = img.shape[1]
        rows, row_rem = divmod(imgshp0, q)
        cols, col_rem = divmod(imgshp1, c)

        if row_rem != 0 or col_rem != 0:
            # Calculate the amount of padding needed for rows and columns
            pad_rows = (q - row_rem) if row_rem != 0 else 0
            pad_cols = (c - col_rem) if col_rem != 0 else 0

            # Pad the image to make it divisible by q rows and c columns
            img = np.pad(img, ((0, pad_rows), (0, pad_cols), (0, 0)), mode='constant')

        boxes = np.array_split(img, q, axis=0)
        split_rows = []
        for row in boxes:
            split_row = np.array_split(row, c, axis=1)
            split_rows.extend(split_row)
        return split_rows
    except AttributeError:
        QMessageBox.warning(
            parent_widget, "NoneType Error", "'NoneType' object has no attribute 'shape'", QMessageBox.Ok
        )
        return []



def calculate_pixel_values(image_parts, num_questions, num_choices):
    global ratio
    q = num_questions // 5
    c = num_choices
    myPixelVal = np.zeros((q, c))
    count_Rows = 0
    count_Column = 0
    selected_answers = []
    total_rows_exceeding_threshold = 0

    if num_questions == 25:
        ratio = 0.6
    if num_questions == 50:
        ratio = 0.7
    if num_questions == 80:
        ratio = 0.8


    for image in image_parts:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        inverted_image = cv2.bitwise_not(gray_image)  # Invert the grayscale image
        totalPixels = cv2.countNonZero(inverted_image)
        myPixelVal[count_Rows][count_Column] = totalPixels
        count_Column += 1
        if count_Column == c:
            count_Rows += 1
            count_Column = 0
    for x in range(q):
        arr = myPixelVal[x]
        max_pix_val = np.amax(arr)
        other_elements = arr[arr < max_pix_val]  # Exclude the max pixel value from the other elements
        if np.any(other_elements > ratio * max_pix_val):
            # print("This row has other box that is greater than 0.9 of the max_pix_val")
            total_rows_exceeding_threshold += 1
        # else:
            # print("All elements are within the threshold.")
        selected_answer = np.argmax(arr)   # Convert index to corresponding letter (A, B, C)
        selected_answers.append(selected_answer)
        print(arr)
    print("Invalid: ", total_rows_exceeding_threshold)
    return selected_answers, total_rows_exceeding_threshold



def warp(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    edges = cv2.Canny(blurred_frame, 50, 150)
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    imgContour = frame.copy()  # Create a copy of the frame for drawing contours
    imgBiggestRectCon = frame.copy()
    cv2.drawContours(imgContour, contours, -1, (0, 255, 0), 2)  # Draw contours on the copied frame

    rectangles = find_rect(contours)



    if rectangles:
        biggestRectCon = rectangles[0]

        cv2.drawContours(imgBiggestRectCon, [biggestRectCon], -1, (0, 255, 0), 2)

        biggestRectCon = reorder(biggestRectCon)

        widthImg = 520
        heightImg = 500
        pt1 = np.float32(biggestRectCon)
        pt2 = np.float32([[0, 0], [widthImg, 0], [0, heightImg], [widthImg, heightImg]])
        matrix = cv2.getPerspectiveTransform(pt1, pt2)
        imgWarpColored = cv2.warpPerspective(frame, matrix, (widthImg, heightImg))
        imgWarp = crop_adjusted(imgWarpColored, 4, 4, 5, 5)

        return imgWarp, imgWarpColored

    return None, None



def crop_adjusted(image, top, bottom, left, right):
    height, width = image.shape[:2]
    cropped = image[top:height-bottom, left:width-right]
    return cropped

