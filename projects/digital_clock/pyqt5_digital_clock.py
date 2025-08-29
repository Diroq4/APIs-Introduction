#PyQt5 Digital Clock
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt #QT IS FOR ALLIGMENT
from PyQt5.QtGui import QFont, QFontDatabase #This import is if we will like to us our onw custom font that can be downloaded to applit it to our label or program

class Digital_clock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self) #label that display the time
        self.timer = QTimer(self) #Add the timer to the clock, keeps track and update the clock
        self.initUI()



    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(350, 400, 300, 100)

#SETTING LAYOUT MANAGER
        vbox = QVBoxLayout()  #Arrange widget vertically
        vbox.addWidget(self.time_label) #This add our label "time_label" to the a layput manager VBOX
        self.setLayout(vbox)

#SETTING THE WAY THE LABLE LOOKS AND APPEAR ON THE WIDGET
        self.time_label.setAlignment(Qt.AlignCenter) #Put the lable right in the middle
        self.time_label.setStyleSheet(#"font-size: 160px;"
                                      #"font-family: Arial;"
                                      "color: #0ef20a;")
        self.setStyleSheet("background-color: black") #We set the background color as black using this line

#SETTING OUR CUSTOPM DONWLOADED FONT
        font_id = QFontDatabase.addApplicationFont("C:/Users/Diroq/OneDrive/Documentos/APIs/projects/digital_clock/DS-DIGIT.TTF") #Is to let the system know where is the font style file
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family, 50) #Set the font and font size
        self.time_label.setFont(my_font) #add the font to the time_label so it will show on the widget

#THIS IS HOW TO UPDATE EVERY SECOND SO IT WILL COUNT AN REFRESH TO KEEP PROVDING THE ACTUAL TIME
        self.timer.timeout.connect(self.update_time) 
        self.timer.start(1000) #This is the miliseconds, so in this case every 1000 miliseconds it will refresh, so it will update every second

        self.update_time()

#SETTING THE TIME AND TIMER
    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP") #This variable is to get the current time from the computer and git it format with the ".toString", the AP is to add AM or PM at the end.
        self.time_label.setText(current_time) #Here we assigned the current time to the label so it will show on the widget
        #The we need to call this function on the main initUI so it will show, this is because that is our main widget where the program is processing and showing the info

if __name__  == '__main__': #From here below is the set up for the window we will show
    app = QApplication(sys.argv)
    clock = Digital_clock()
    clock.show() #Shows the window
    sys.exit(app.exec_()) #If we dont have this line the window will show for a second and then will close, this is to keep it on screen
