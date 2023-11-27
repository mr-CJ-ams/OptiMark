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

Here is an overview of the logic and interactions between the 
users and the software based on the provided code:

1. StartScreen:
   • When the application starts, it displays the StartScreen.
   • The StartScreen provides three options:
      i. About: Opens a dialog box with information about the application.
      ii. Download Template: Opens the DownloadTemplateScreen, where users can download question templates for different question counts (25, 50, or 100 items).
      iii. Start Test: Opens the CheckBoxesScreen, where users can select the number of questions (25, 50, or 100) and proceed with the test.

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/7826d467-e1dd-4012-ad7a-76e1df0d4c96)

2. DownloadTemplateScreen:
• This screen shows the downloadable question templates for 
different question counts (25, 50, or 100 items).
• Users can click on the "Download" button next to each 
template to download the corresponding PDF file

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/974843fb-c8a8-4492-bc2e-3a5d183b8181)

3. CheckBoxesScreen:
• This screen allows users to select the number of questions for the test (25, 50, or 100).
• Upon selecting the number of questions, the screen dynamically creates rows of checkboxes based on the selected count. Each row represents a question, and each row has three options (choices A, B, and C) represented by radio buttons.
• Users must answer all questions by selecting one option (radio button) per row.
• The "Next" button is used to proceed to the CaptureScreen after answering the questions
