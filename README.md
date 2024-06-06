# OptiMark
OptiMark: Unleash the Power of Precision in Grading! This optical mark recognition program 
revolutionizes the way answer sheets are scored. Say goodbye to manual calculations and hello to 
lightning-fast, accurate results. With OptiMark, effortlessly process and analyze bubbled answer 
sheets, ensuring a seamless grading experience. Let the technology do the heavy lifting while you 
focus on what truly matters – empowering students to shine. Discover the future of automated 
scoring with OptiMark!

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/1429e08a-a438-411e-97a2-a2952fe00808)

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/0996a331-27f5-4b4d-898b-9cd0baaf2d86)

The code is written in Python using the PyQt5 library to create a 
graphical user interface (GUI) application. The application 
appears to be an Optical Mark Recognition (OMR) system for 
capturing and analyzing user-inputted answers from a form.


# Summary of OptiMark Software Functions and Features:

OptiMark offers the following functions:

1. Optical Mark Recognition (OMR):

• Efficiently scans and captures data from answer sheets containing marked bubbles.

• Detects and interprets bubble markings accurately and swiftly

2. Scanning and Data Capture:

• Seamlessly integrates with scanning devices to digitize answer 
sheets.

• Ensures high-quality image capture and precise extraction of 
bubble data.

3. Answer Key Configuration:

• Allows users to define answer keys or scoring rubrics for 
automated result calculation.

• Supports flexible marking schemes, including single or multiple 
correct answers per question.

4. Result Calculation:

• Automates the calculation of individual and aggregate scores 
based on the provided answer keys.

• Generates accurate and reliable results, saving time and effort 
for educators.

5. Error Detection and Verification:

• Can detect multiple answers and rejects it

• Includes built-in mechanisms to detect potential scanning or 
marking errors.

• Provides verification tools for reviewing and validating 
captured data, ensuring data accuracy.



# Here is an overview of the logic and interactions between the users and the software based on the provided code:

# 1. StartScreen:
   
   • When the application starts, it displays the StartScreen.
   
   • The StartScreen provides three options:
   
      i. About: Opens a dialog box with information about the application.
   
      ii. Download Template: Opens the DownloadTemplateScreen, where users can download question templates for different question counts (25, 50, 75, or 100 items).
   
      iii. Start Test: Opens the CheckBoxesScreen, where users can select the number of questions (25, 50, 75, or 100) and proceed with the test.

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/7826d467-e1dd-4012-ad7a-76e1df0d4c96)

# 2. DownloadTemplateScreen:
   
• This screen shows the downloadable question templates for different question counts (25, 50, 75, or 100 items).

• Users can click on the "Download" button next to each template to download the corresponding PDF file

![Screenshot 2024-06-07 004603](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/263f71d0-5cd2-4687-8437-5d4bb9c18855)


# 3. CheckBoxesScreen:
   
• This screen allows users to select the number of questions for the test (25, 50, 75, or 100).

![Screenshot 2024-06-07 004517](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/b8149fae-c77b-4dff-9eff-57cd935ce1d0)


• Upon selecting the number of questions, the screen dynamically creates rows of checkboxes based on the selected count. Each row represents a question, and each row has three options (choices A, B, and C) represented by radio buttons.

• Users must fill all items by selecting one option (radio button) per row.

![image](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/0ce9a43c-40a1-488a-b502-1b244392facc)


![image](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/468219a5-2ed5-4e97-86ea-8f402d446b65)

![image](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/ef8e5825-44c7-4b5b-b869-87c277e1abec)


• Make sure your Webcam is connected to your computer to proceed to the CaptureScreen



• The "Next" button is used to proceed to the CaptureScreen after answering the questions



# 4. CaptureScreen:
   
• This screen displays a webcam feed showing the user taking the test using a webcam.

• When the "Freeze" button is pressed, the frame from the webcam is frozen, and the system processes the captured frame to extract answers using image processing techniques.

• The system divides the captured frame into different sections corresponding to different parts of the answer sheet (top and bottom thirds).

• It then processes each section to split the image into individual parts, each representing a question.

• The system calculates the selected answers for each part/question based on the user's choice (A, B, or C).

• The user can press the "Unfreeze" button to unfreeze the webcam and continue taking the test.

• The system displays the selected answers and the user's score (number of correct answers) on the screen

![Screenshot 2024-06-07 004256](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/87afc29f-9817-4ee7-b3a3-6779e22e7669)

![Screenshot 2024-06-07 004336](https://github.com/mr-CJ-ams/OptiMark-App/assets/110215820/e81de8b4-3e7e-4bca-90b1-e99b031c3f43)


