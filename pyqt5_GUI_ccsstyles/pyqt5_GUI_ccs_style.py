#CCS Style edits
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QHBoxLayout  #Here it will show the import for radio buttons QRadioButton, QButtonGroup (this is to group together multiple buttons), it is imports are for the window to be showned and edit


class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("CSS Styles GUI") #This is how the window will appear on top, like the name of the program
        self.accessibleDescription
        self.push1 = QPushButton("#1")
        self.push2 = QPushButton("#2")
        self.push3 = QPushButton("#3")
        self.initUI()

    def initUI(self): #Creating this function is a good practice to organize and create the user interface "UI"
        central_widget = QWidget() #Since we are using QWidget there is no need to specify dimension this is a widget manager will do it automatically
        self.setCentralWidget(central_widget)

        hbox = QHBoxLayout() #Here we are specifing the the buttons will shor horizontally 
        hbox.addWidget(self.push1) #Here we add the buttons to the widget
        hbox.addWidget(self.push2)
        hbox.addWidget(self.push3)

#APPLY THE FORMAT TO BE CENTER O HOW WE SPECIFY
        central_widget.setLayout(hbox) #Without setting a layout, Qt would not know how to place or arrange the widgets inside the container.
        #is what activates the layout on the central widget, ensuring that the buttons (push1, push2, push3) appear side-by-side inside the window.

def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()