# Line edits / Text boxes
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton #Here it will show the import for radio buttons QRadioButton, QButtonGroup (this is to group together multiple buttons), it is imports are for the window to be showned and edit


class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Line Edit GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.initUI()

    def initUI(self): #Creating this function is a good practice to organize and create the user interface "UI"
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.line_edit.setStyleSheet("font-size: 25px;"
                                     "font-family: Roboto")
        self.button.setGeometry(210, 10, 200, 40)
        self.button.setStyleSheet("font-size: 18px;"
                                  "font-family: Roboto")
        self.line_edit.setPlaceholderText("Enter your name") #This is a place holder that will show on the text box, prior to someone that can write on it, like on the background
        
#In this line we are connecting the click on the submit button to the the action of the function specify
        self.button.clicked.connect(self.submit)
    
    def submit(self):
        # This is other way that is by creating a local variable.
        # text = self.line_edit.text()
        # print(f"{text}")
        print(f"{self.line_edit.text()}") #.TEXT method its a must to display the text


def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()