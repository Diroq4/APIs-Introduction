# Python GUI introduction using PYQt5
# PyQt5.QtWidgets are the building block for a PyQt5 application
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #This imports are for the window to be showned and edit
from PyQt5.QtGui import QFont #This import will for for lables, basically to edit them (size,font, etc...)
from PyQt5.QtCore import Qt #This class is use for alignments 

class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Lables GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 400, 400) #This is the geometri and were it will appear when executing (x , y, width, height)

        label = QLabel("Hello", self) #Label refers to a text we can show on the window, on this line we is how to wrtie something to show
        label.setFont(QFont("Arial", 50)) #Here we procide the type of font and the size, in the same order
        label.setGeometry(0,0, 400, 100) #This is the geometri and were it will appear when executing (x , y, width, height)
        label.setStyleSheet("color: #e06336;"
                            "background-color: #47322b;"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;") 
#EVERTHING ABOVE THIS: is to edit and modify the color of letters, back ground, type of text, etc...

#ALIGMENT
        # Is this the alingment options and how to do it on a VERTICAL MANNER
        # label.setAlignment(Qt.AlignTop) #This will aling it VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) #This will aling it VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) #This will aling it VERTICALLY CENTER

        # Is this the alingment options and how to do it on a HORIZONTAL MANNER
        # label.setAlignment(Qt.AlignRight) #This will aling it HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) #This will aling it HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) #This will aling it HORIZONTALLY LEFT

        #Here is how to convine Horizontal and Vertical in the same line of code using "|"
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) #CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #CENTER & CENTER
        label.setAlignment(Qt.AlignCenter) #SHORT CUT FOR CENTER & CENTER ALIGMENT


def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()