# Python GUI introduction using PYQt5
# PyQt5.QtWidgets are the building block for a PyQt5 application
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel #This imports are for the window to be showned and edit
from PyQt5.QtGui import QPixmap #This is important to add import iimages and provide functionality to load images

class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Image GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)

        label = QLabel(self) #Label refers to a text we can show on the window, on this line we is how to wrtie something to show, in this case we convert an image to a lable se it shows the picture
        label.setGeometry(0, 0, 250, 250) #This is the geometri and were it will appear when executing (x , y, width, height)

#In this following text is to pass the image to the label, we are showing images as labels since is easier
        pixmap = QPixmap("C:/Users/diego.roses/OneDrive - OMRON/Documents/mycourse/APIs_course/pyqt5_GUI_Images/moto_pic.jpg")
        label.setPixmap(pixmap)
#This is use to scale the image to show completely
        label.setScaledContents(True)

#POSITIONING CENTER
        label.setGeometry((self.width() - label.width()) // 2, (self.height() - label.height()) // 2, label.width(), label.height())



def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()