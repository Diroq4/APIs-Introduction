# Python GUI introduction using PYQt5
# PyQt5.QtWidgets are the building block for a PyQt5 application
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow #This imports are for the window to be showned and edit
from PyQt5.QtGui import QIcon #This is important to add an icon to the window

class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("My first GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)
        self.setWindowIcon(QIcon("C:/Users/Diroq/OneDrive/Documentos/APIs/pyqt5_GUI_intro/moto_pic.jpg")) #This will set the icone for the GUI

def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()