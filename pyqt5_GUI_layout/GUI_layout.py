# Layout in PyQt5
import sys 
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout #This imports are for the window to be showned and edit
#for layouts the new imports were QVBoxLayout, QHBoxLayout, QGridLayout, they allow is to work with layouts


class MainWindow(QMainWindow): #This is the class we need to create a window and display it to the user of modify it
    def __init__(self): #Constructor
        super().__init__()
        self.setWindowTitle("Layout GUI") #This is how the window will appear on top, like the name of the program
        self.setGeometry(700, 300, 600, 500) #This is the geometri and were it will appear when executing (x , y, width, height)
        self.initUI()

    def initUI(self): #Creating this function is a good practice to organize and create the user interface "UI"
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)
        label2 = QLabel("#2", self)
        label3 = QLabel("#3", self)
        label4 = QLabel("#4", self)

        label1.setStyleSheet("background-color: #fcba03;")
        label2.setStyleSheet("background-color: #4287f5;")
        label3.setStyleSheet("background-color: #eb4034;")
        label4.setStyleSheet("background-color: #32a852;")

# VERTICAL LAYOUT MANAGER
        # vbox = QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)

        # central_widget.setLayout(vbox)

# HORIZONTAL LAYOUT MANAGER
        # hbox = QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)

        # central_widget.setLayout(hbox)

#GRID LAYOUT MANAGER
        grid = QGridLayout() 
        grid.addWidget(label1, 0, 0) #With GRIDS we need to specify the ROW and COLUM in the same order
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 1, 0)
        grid.addWidget(label4, 1, 1)

        central_widget.setLayout(grid)

def main(): #This function basically when we begin the program it will start/execute the application(Windows)
    app = QApplication(sys.argv)
    window = MainWindow() #This call the class created 
    window.show() #This will show the window, without this the window created wont appear on our display
    sys.exit(app.exec_()) #Ensure clean method of our program, the exec_ will allow us to press buttons exit, minimize the window and interact with it.

if __name__ == "__main__":
    main()