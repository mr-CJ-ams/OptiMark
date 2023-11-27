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
   
• This screen shows the downloadable question templates for different question counts (25, 50, or 100 items).

• Users can click on the "Download" button next to each template to download the corresponding PDF file

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/974843fb-c8a8-4492-bc2e-3a5d183b8181)

3. CheckBoxesScreen:
   
• This screen allows users to select the number of questions for the test (25, 50, or 100).

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/b9fa92a1-9675-4376-8094-78c7a6b0768c)


• Upon selecting the number of questions, the screen dynamically creates rows of checkboxes based on the selected count. Each row represents a question, and each row has three options (choices A, B, and C) represented by radio buttons.

• Users must fill all items by selecting one option (radio button) per row.

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/51fa4102-c77d-4da2-aeed-23b8638be120)

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/16e2c60e-fede-4177-be6a-0231943059e1)

• Make sure your Webcam is connected to your computer to proceed to the CaptureScreen

![image](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/ce9d7063-e1d8-4dde-b874-03f832368eb3)


• The "Next" button is used to proceed to the CaptureScreen after answering the questions



4. CaptureScreen:
• This screen displays a webcam feed showing the user taking the test using a webcam.

• When the "Freeze" button is pressed, the frame from the webcam is frozen, and the system processes the captured frame to extract answers using image processing techniques.

• The system divides the captured frame into different sections corresponding to different parts of the answer sheet (top and bottom thirds).

• It then processes each section to split the image into individual parts, each representing a question.

• The system calculates the selected answers for each part/question based on the user's choice (A, B, or C).

• The user can press the "Unfreeze" button to unfreeze the webcam and continue taking the test.

• The system displays the selected answers and the user's score (number of correct answers) on the screen

![Screenshot 2023-07-20 015406](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/c6d9f36b-c344-4228-9140-c0bbd93e9619)

![Screenshot 2023-07-20 015432](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/752b753e-5efe-44a5-9d7e-97095bf76f66)

![Screenshot 2023-07-20 015513](https://github.com/mr-CJ-ams/OptiMark/assets/110215820/1a0deeb6-1f67-45f6-bc2e-a9e9b20286bd)
