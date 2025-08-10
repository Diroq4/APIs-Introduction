# Layout in PyQt5
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel #This imports are for the window to be showned and edit
#For Pushbuttons the new imports: QPushButton and QLabel


class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("PushButton GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)
        self.button = QPushButton("Click here", self) #It is better to declare the button on the constructor as a global varibale and the fucntion bellow is just to edit
        self.label = QLabel("Hello", self)
        self.initUI()

    def initUI(self): #Creating this function is a good practice to organize and create the user interface "UI"
        self.button.setGeometry(200, 175, 200, 100)
        self.button.setStyleSheet("font-size: 20px;") #Just doing the font from the buttom bigger
        self.button.clicked.connect(self.on_click) #Here is how we link the function below to the button () on any fucntion just by calling the name of it

        self.label.setGeometry(265, 250, 200, 100)
        self.label.setStyleSheet("font-size: 30px;")

    def on_click(self):
        self.label.setText("Goodbye!") #This is how to change the label text from HELLO to GOODBYE in this case

    # def on_click(self): #This is the fucntion that we arrange to the fucntion were we crete the button 
    #     print("Buttom is working!")
    #     self.button.setText("Clicked!")
    #     self.button.setDisabled(True) #This is how we can diable the button when the action assigned to it has been completed, in this case when clicking on it

def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()