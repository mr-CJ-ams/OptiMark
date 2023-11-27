import sys
import os
from PyQt5.uic import loadUi
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QLabel, QButtonGroup, QRadioButton, QGridLayout, QWidget, QMessageBox, QVBoxLayout, QScrollArea
import numpy as np
import cv2
import img_processing
import utlis
import shutil


# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class StartScreen(QDialog):
    def __init__(self):
        super(StartScreen, self).__init__()
        loadUi(resource_path("C://Users//User//OneDrive//Desktop//OM//startscreen.ui"), self)
        # self.image.setPixmap(QPixmap(''))
        self.about.clicked.connect(lambda: utlis.aboutapp(self))
        self.download_temp.clicked.connect(lambda: utlis.show_window(widget, DownloadTemplateScreen))
        self.start.clicked.connect(lambda: utlis.show_window(widget, CheckBoxesScreen))

        email_link = 'mailto:ubshsgr12stemamaquinc@gmail.com'
        github_link = 'https://github.com/mr-CJ-ams'
        web_link = 'https://mr-cj-ams.github.io/OptiMarkTemplate.github.io/'

        self.emailLayout.clicked.connect(lambda: utlis.gotolink(self, email_link))
        self.githubLayout.clicked.connect(lambda: utlis.gotolink(self, github_link))
        self.download.clicked.connect(lambda: utlis.gotolink(self, web_link))

        self.UiComponents()

    def UiComponents(self):
        self.download_temp.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-download-from-the-cloud-48 (1).png")))
        self.download_temp.setIconSize(QtCore.QSize(40, 40))

        self.start.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-start-menu-48.png")))
        self.start.setIconSize(QtCore.QSize(40, 40))

        self.about.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-about-48.png")))
        self.about.setIconSize(QtCore.QSize(40, 40))

        self.emailLayout.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\email (1).png")))
        self.emailLayout.setIconSize(QtCore.QSize(30, 30))

        self.githubLayout.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\github.png")))
        self.githubLayout.setIconSize(QtCore.QSize(35, 35))

class DownloadTemplateScreen(QDialog):
    def __init__(self):
        super(DownloadTemplateScreen, self).__init__()
        loadUi(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\downloadTemplate.ui"), self)
        self.back_button.clicked.connect(lambda: utlis.show_window(widget, StartScreen))

        itms25 = QPixmap(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\25_items.png"))
        scaled_pixmap_itms25 = itms25.scaled(351, 591)  # Set the desired width and height

        itms50 = QPixmap(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\50_items.png"))
        scaled_pixmap_itms50 = itms50.scaled(351, 591)  # Set the desired width and height

        itms80 = QPixmap(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\80_items.png"))
        scaled_pixmap_itms100 = itms80.scaled(351, 591)  # Set the desired width and height


        self.label_25itms.setPixmap(scaled_pixmap_itms25)
        self.label_50itms.setPixmap(scaled_pixmap_itms50)

        pdf_file_path_25itms = resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\AnsSheet25.pdf")
        pdf_file_path_50itms = resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\AnsSheet50.pdf")

        # Create a QPushButton
        self.download25itms.clicked.connect(lambda: self.download_pdf(pdf_file_path_25itms))
        self.download50itms.clicked.connect(lambda: self.download_pdf(pdf_file_path_50itms))

        self.UiComponents()
    def UiComponents(self):
        self.download25itms.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-download-from-the-cloud-48 (1).png")))
        self.download25itms.setIconSize(QtCore.QSize(40, 40))

        self.download50itms.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-download-from-the-cloud-48 (1).png")))
        self.download50itms.setIconSize(QtCore.QSize(40, 40))

        self.back_button.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-left-26.png")))
        self.back_button.setIconSize(QtCore.QSize(100, 100))

    def download_pdf(self, pdf_file_path):
        # Define the PDF destination folder
        destination_folder = os.path.expanduser("~\\Downloads")

        # Extract the PDF filename from the path
        pdf_filename = os.path.basename(pdf_file_path)

        # Construct the destination path
        destination_path = os.path.join(destination_folder, pdf_filename)

        # Copy the file to the Downloads folder
        try:
            shutil.copy(pdf_file_path, destination_path)
            QMessageBox.information(self, "Download", "Download Successful")
        except Exception as e:
            error_message = "Error occurred while downloading the file:\n" + str(e)
            QMessageBox.critical(self, "Download Error", error_message)



class CheckBoxesScreen(QDialog):
    def __init__(self):
        super(CheckBoxesScreen, self).__init__()
        self.checkboxes = None
        loadUi(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\checkboxes.ui"), self)
        self.items25.clicked.connect(lambda: self.gotocheckboxes(25))
        self.items50.clicked.connect(lambda: self.gotocheckboxes(50))
        self.back_button.clicked.connect(lambda: utlis.show_window(widget, StartScreen))


        self.num_questions = None  # Initialize num_questions attribute to None

        self.next.clicked.connect(self.gonext)


        scroll_area = QScrollArea()
        scroll_area.setStyleSheet(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\background-color: rgba(0, 0, 0,0);"))
        self.verticalLayout.addWidget(scroll_area)

        scroll_widget = QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_area.setWidgetResizable(True)

        scroll_layout = QVBoxLayout(scroll_widget)

        grid_layout = QGridLayout()
        grid_layout.setAlignment(Qt.AlignTop)
        self.scroll_layout = scroll_layout
        self.grid_layout = grid_layout
        scroll_layout.addLayout(self.grid_layout)

        self.UiComponents()

    def UiComponents(self):
        self.back_button.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-left-26.png")))
        self.back_button.setIconSize(QtCore.QSize(100, 100))

    def gotocheckboxes(self, num):
        self.num_questions = num
        self.update_checkboxes()

    def update_checkboxes(self):
        # Clear any existing checkboxes
        while self.grid_layout.count():
            item = self.grid_layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        num_choices = 3

        self.checkboxes = []
        for question_index in range(self.num_questions):
            question_label = QLabel(f"{question_index + 1}.")
            question_label.setStyleSheet("QLabel {"
                                         "font-size: 20px;"
                                         "}")
            self.grid_layout.addWidget(question_label, question_index + 1, 0, Qt.AlignCenter)

            checkboxes_row = []
            button_group = QButtonGroup(self)  # Create a button group for each row

            for choice_index in range(num_choices):
                radio_button = QRadioButton()
                radio_button.setStyleSheet("""
                                QRadioButton {
                                    font-size: 20px;
                                }

                                QRadioButton::indicator {
                                    width: 30px;
                                    height: 30px;
                                }

                            """)
                checkboxes_row.append(radio_button)
                self.grid_layout.addWidget(radio_button, question_index + 1, choice_index + 1, Qt.AlignCenter)
                button_group.addButton(radio_button)

            button_group.setExclusive(True)  # Allow only one radio button to be checked in each row
            self.checkboxes.append(checkboxes_row)

    def gonext(self):
        if self.num_questions is not None:  # Check if num_questions is set
            video_capture_index = 1  # Specify the desired index for VideoCapture

            video_capture = cv2.VideoCapture(video_capture_index)

            if video_capture.isOpened():
                all_checked = True
                unchecked_rows = []  # Store the indices of unchecked rows

                # Check if all checkboxes are checked
                for row_index, checkboxes_row in enumerate(self.checkboxes):
                    row_checked = any(checkbox.isChecked() for checkbox in checkboxes_row)
                    if not row_checked:
                        all_checked = False
                        unchecked_rows.append(row_index)

                if all_checked:
                    chosen_checkboxes = [
                        chr(ord('A') + choice_index)
                        for question_index, checkboxes_row in enumerate(self.checkboxes)
                        for choice_index, checkbox in enumerate(checkboxes_row)
                        if checkbox.isChecked()
                    ]
                    capture_screen = CaptureScreen(chosen_checkboxes, self.num_questions)
                    widget.addWidget(capture_screen)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                else:
                    QMessageBox.warning(self, "Warning", "Please check all the radio buttons.")

                    # Change the text color of the question_label for unchecked rows to red
                    for row_index in unchecked_rows:
                        question_label = self.grid_layout.itemAtPosition(row_index + 1, 0).widget()
                        question_label.setStyleSheet("color: red; font-size: 20px;")
            else:
                QMessageBox.warning(self, "Warning", "Connect your webcam to your device.")

            video_capture.release()
        else:
            QMessageBox.warning(self, "Warning", "Please select the number of questions first.")


class CaptureScreen(QDialog):
    def __init__(self, answer_key, num_questions):
        super(CaptureScreen, self).__init__()
        loadUi(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\capture.ui"), self)
        self.back_button.clicked.connect(self.goback)

        self.answer_key = answer_key  # Assign answer_key to self.answer_key


        ansk_layout = QVBoxLayout()

        grid_layout = QGridLayout()
        row = 0
        col = 0

        if num_questions == 80:
            clm = 16
        if num_questions == 50:
            clm = 10
        if num_questions == 25:
            clm = 5

        question_number = 1

        for key in self.answer_key:  # Use self.answer_key here
            key_label = QLabel(f"{question_number}. {key}")  # Add the question number
            key_label.setStyleSheet("font-size: 15px; color: black;")
            grid_layout.addWidget(key_label, row, col)
            row += 1
            if row == clm:
                row = 0
                col += 1
            question_number += 1

        ansk_layout.addLayout(grid_layout)
        ansk_layout.addStretch(1)  # Add stretch to align to the top
        self.answerkeyLayout.addLayout(ansk_layout)


        # Initialize camera capture
        self.cap = cv2.VideoCapture(1)  # Modify the camera index as needed
        self.camera_label = QLabel()   # Create a QLabel to display the camera frame
        self.camera_label.setAlignment(Qt.AlignTop)
        self.cameraframeLayout.addWidget(self.camera_label)   # Add the camera frame to the main_layout


        # Start the camera capture timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(lambda: self.update_frame(num_questions, answer_key))
        self.timer.start(30)  # Update frame every 30 milliseconds

        # Freeze Button
        self.freeze.clicked.connect(self.freeze_video)

        # Unfreeze Button
        self.unfreeze.clicked.connect(self.unfreeze_video)

        # Flag to indicate whether the capture is frozen or not
        self.frozen = False
        self.frozen_frame = None
        self.webcam_connected = False

        self.grid_layout = QGridLayout()  # Create a QGridLayout for key labels
        self.grid_layout.setAlignment(Qt.AlignTop)  # Align key labels to the bottom
        self.selectedanswerLayout.addLayout(self.grid_layout)


        self.score_label = QLabel()
        self.score_label.setStyleSheet("font-size: 30px; color: black;")
        # self.score_label.setAlignment(Qt.AlignRight)
        self.scoreLayout.addWidget(self.score_label)

        self.percentage_label = QLabel()
        self.percentage_label.setStyleSheet("font-size: 15px; color: black;")
        # self.score_label.setAlignment(Qt.AlignRight)
        self.percentageLayout.addWidget(self.percentage_label)

        self.UiComponents()

    def UiComponents(self):
        self.back_button.setIcon(QtGui.QIcon(resource_path("C:\\Users\\User\\OneDrive\\Desktop\\OM\\icons8-left-26.png")))
        self.back_button.setIconSize(QtCore.QSize(100, 100))

    def update_frame(self, num_questions, answer_key):

        if not self.webcam_connected:
            success = self.cap.open(1)
            if success:
                self.webcam_connected = True
                QMessageBox.information(self, "Webcam Connected", "Your webcam is connected")
            else:
                return

        success, frame = self.cap.read()
        if not success:
            self.webcam_connected = False
            QMessageBox.warning(self, "Webcam Disconnected", "Your webcam is disconnected")
            return

        if self.frozen:
            frozen_frame = np.copy(self.frozen_frame)  # Create a copy of the frozen frame

            result = self.img_processing(frozen_frame, num_questions, answer_key)  # Call the function to process the frozen frame
            imgResult = result[0]
            final_score = result[1]
            all_selected_answers = result[2]
        else:
            imgResult = frame.copy()  # Use the original frame without processing
        if self.frozen:
            self.score_label.setText(f"Score: {final_score}")
            self.score_label.setAlignment(Qt.AlignCenter)

            rate = (final_score / num_questions) * 100

            self.percentage_label.setText(f"{rate}%")
            self.percentage_label.setAlignment(Qt.AlignCenter)

            self.grid_layout.setEnabled(True)

            row = 0
            col = 0

            if num_questions == 80:
                clm = 16
            if num_questions == 50:
                clm = 10
            if num_questions == 25:
                clm = 5

            question_number = 1

            while self.grid_layout.count():
                item = self.grid_layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.hide()
                    # widget.setParent(None)

            for key, selected_answer in zip(answer_key, all_selected_answers):
                key_label = QLabel(f"{question_number}. {selected_answer}")  # Add the question number
                key_label.setStyleSheet("font-size: 15px; color: black;")
                if selected_answer != key:
                    key_label.setStyleSheet("font-size: 15px; color: red")  # Change text color to red if not the same as answer_key
                self.grid_layout.addWidget(key_label, row, col)
                row += 1
                if row == clm:
                    row = 0
                    col += 1
                question_number += 1

        else:
            self.score_label.clear()
            self.percentage_label.clear()
            # Clear the grid_layout when the camera frame is not frozen
            self.grid_layout.setEnabled(False)

            # Hide the widgets within the grid layout
            for i in range(self.grid_layout.count()):
                item = self.grid_layout.itemAt(i)
                widget = item.widget()
                if widget:
                    widget.hide()



        rgb_image = cv2.cvtColor(imgResult, cv2.COLOR_BGR2RGB)


        height, width, _ = rgb_image.shape
        qimage = QImage(rgb_image.data, width, height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.camera_label.setPixmap(pixmap)

    def img_processing(self, frame, num_questions, answer_key):
        _, imgWarpColored = img_processing.warp(frame)

        if imgWarpColored is None:
            QMessageBox.warning(self, "No Rectangle Found", "No rectangles were found in the image.", QMessageBox.Ok)
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()



        top_third2, top_third3, bottom_third1, bottom_third2, bottom_third3 = img_processing.divide_rect_into_thirds(imgWarpColored)


        t1, _ = img_processing.warp(top_third2)
        _, t1= cv2.threshold(t1, 127, 255, cv2.THRESH_BINARY)

        t2, _ = img_processing.warp(top_third3)
        _, t2 = cv2.threshold(t2, 127, 255, cv2.THRESH_BINARY)

        b1, _ = img_processing.warp(bottom_third1)
        _, b1 = cv2.threshold(b1, 127, 255, cv2.THRESH_BINARY)

        b2, _ = img_processing.warp(bottom_third2)
        _, b2 = cv2.threshold(b2, 127, 255, cv2.THRESH_BINARY)

        b3, _ = img_processing.warp(bottom_third3)
        _, b3 = cv2.threshold(b3, 127, 255, cv2.THRESH_BINARY)


        # Split each adjusted largest rectangle into parts using vsplit and hsplit based on num_questions

        top_third2_parts = img_processing.splitBoxes(t1, num_questions, 3, self)
        if not top_third2_parts:
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()

        top_third3_parts = img_processing.splitBoxes(t2, num_questions, 3, self)
        if not top_third3_parts:
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()

        bottom_third1_parts = img_processing.splitBoxes(b1, num_questions, 3, self)
        if not bottom_third1_parts:
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()

        bottom_third2_parts = img_processing.splitBoxes(b2, num_questions, 3, self)
        if not bottom_third2_parts:
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()

        bottom_third3_parts = img_processing.splitBoxes(b3, num_questions, 3, self)
        if not bottom_third3_parts:
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()


        # Calculate pixel values and selected answers for each part
        top_third2_selected_answers, inv1 = img_processing.calculate_pixel_values(top_third2_parts, num_questions, 3)
        top_third3_selected_answers, inv2 = img_processing.calculate_pixel_values(top_third3_parts, num_questions, 3)
        bottom_third1_selected_answers, inv3 = img_processing.calculate_pixel_values(bottom_third1_parts, num_questions, 3)
        bottom_third2_selected_answers, inv4 = img_processing.calculate_pixel_values(bottom_third2_parts, num_questions, 3)
        bottom_third3_selected_answers, inv5 = img_processing.calculate_pixel_values(bottom_third3_parts, num_questions, 3)

        if any(inv != 0 for inv in (inv1, inv2, inv3, inv4, inv5)):
            QMessageBox.warning(self, "Invalid", "Blank items and multiple answers per question not allowed  ", QMessageBox.Ok)
            self.unfreeze_video()  # Unfreeze the camera frame
            return frame.copy()

        # Combine all selected answers
        all_selected_answers = (
                [chr(ord('A') + answer) for answer in top_third2_selected_answers]
                + [chr(ord('A') + answer) for answer in top_third3_selected_answers]
                + [chr(ord('A') + answer) for answer in bottom_third1_selected_answers]
                + [chr(ord('A') + answer) for answer in bottom_third2_selected_answers]
                + [chr(ord('A') + answer) for answer in bottom_third3_selected_answers]
        )
        # Calculate total score
        total_score = sum(1 for selected, key in zip(all_selected_answers, answer_key) if selected == key)

        # Print all selected answers and total score
        print("All selected answers:")
        print(all_selected_answers)
        print("Total score:", total_score)

        imgResult = imgWarpColored.copy()

        # Display imgResult frame
        rgb_image = cv2.cvtColor(imgResult, cv2.COLOR_BGR2RGB)
        height, width, _ = rgb_image.shape
        qimage = QImage(rgb_image.data, width, height, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.camera_label.setPixmap(pixmap)


        return imgResult, total_score, all_selected_answers

    def freeze_video(self):
        if not self.frozen:
            _, self.frozen_frame = self.cap.read()
            self.frozen = True
            self.score_label.show()

    def unfreeze_video(self):
        self.frozen = False
        self.score_label.close()  # Hide the score label

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            self.freeze_video()
        elif event.key() == Qt.Key_D:
            self.unfreeze_video()

    def closeEvent(self, event):
        self.cap.release()
        self.timer.stop()
        super().closeEvent(event)

    def goback(self):
        self.timer.stop()
        self.cap.release()
        back = CheckBoxesScreen()
        widget.addWidget(back)
        widget.setCurrentIndex(widget.currentIndex() + 1)


app = QApplication(sys.argv)
welcome = StartScreen()
widget = QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(970)
widget.setFixedWidth(1900)
widget.show()
try:
    sys.exit(app.exec_())
except Exception as e:
    print("An error occurred:", str(e))
