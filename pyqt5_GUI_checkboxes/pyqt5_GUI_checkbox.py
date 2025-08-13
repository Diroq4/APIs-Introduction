import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QLabel #QCheckBox is the import we need to add check boxes
from PyQt5.QtCore import Qt #I dont understand but this one to, it contains non GUI clases relevant for PyQt application

class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Checkboxes GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)
        self.checkbox = QCheckBox("Do you like pizza?", self) #First the message we want to show and then "self" where we are going to be adding the check box
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.checkbox.setGeometry(10,0, 600, 100)
        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.label.setGeometry(10, 100, 600, 100)
        
        #The box is not check by default if we want to initialize with the boxed check we need to add the following line
        # self.checkbox.setChecked(True)

        #This is how we connect the action of checking to the box to a function, the fucntion is the DEF CHECKBOX_CHANGE
        self.checkbox.stateChanged.connect(self.checkbox_change)

        #This a test for me so when the box is checked it will display the message
        self.checkbox.stateChanged.connect(self.on_click)

    def checkbox_change(self, state):
        if state == Qt.Checked: #THIS Qt.Checked IS TO LET THE SYSTEM NOW THAT THE BOX HAS BEEN CHECK
            print("Yes you do!")
        else:
            print("You don't!")

    #This fucntion it to show the message above on the GUI
    def on_click(self, state):
        if state == Qt.Checked:
            self.label.setText("You do like Pizza!")
        else:
            self.label.setText("")

def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()