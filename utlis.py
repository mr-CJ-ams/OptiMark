from PyQt5.QtWidgets import QStackedWidget, QMessageBox
import webbrowser




def show_window(widget: QStackedWidget, screen_class):
    screen = screen_class()
    widget.addWidget(screen)
    widget.setCurrentIndex(widget.currentIndex() + 1)

def gotolink(self, web_link):
    webbrowser.open(web_link)

def aboutapp(self):
    msg = QMessageBox(self)
    msg.setWindowTitle("About")
    msg.setText("""
    Introducing OptiMark: Your Visionary Solution for Seamless Mark Recognition!

    Are you tired of the mind-numbing task of manually grading answer sheets? Do you yearn for a magical solution that can save you from the never-ending stacks of papers? Look no further, because OptiMark is here to turn your grading nightmares into a breeze of pure delight! OptiMark, the brainchild of a genius with a touch of madness, is not your ordinary answer sheet checker. No, it's an eccentric masterpiece that combines Computer Vision, a sprinkle of quirkiness, and a dash of secret sauce to revolutionize the way you assess your students' performance.
""")
    msg.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(23, 209, 39, 255), stop:1 rgba(255, 255, 255, 255)); font: 15pt; color: rgb(0, 0, 0);")
    msg.setGeometry(1380, 140, 480, 800)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setDefaultButton(QMessageBox.Ok)
    msg.exec_()







