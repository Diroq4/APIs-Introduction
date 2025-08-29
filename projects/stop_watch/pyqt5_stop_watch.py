#Stop Watch
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLayout, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel ("00:00:00:00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.restart_button = QPushButton("Restart", self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self): #On here we are editing only the way that it looks not fuctions only apariencia and connect the actions tot he functions
        self.setWindowTitle("Stop Watch") #Change the name that show on top of the window
        self.setGeometry(600, 400, 300, 100) #This is the geometri and were it will appear when executing (x , y, width, height)
        
        vbox = QVBoxLayout() #Order the buttons automatically with the layout import
        vbox.addWidget(self.time_label)

        self.setLayout(vbox) #We pass the layout created (VBOX) so it will arrange it
        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout() #Here we are doing that the buttons are shown below the watch, so we arrangement in order and then see line 32
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.restart_button)

        vbox.addLayout(hbox) #We add the buttons to the vertical layout so they will show below and order, it basically arrange verticaly depending on the time label VBOX

        self.setStyleSheet("""
            QPushButton, QLabel{
                padding: 20px;
                 font-weight: bold;
            }
                           
            QPushButton{
                font-size: 50px;
            }
                           
            QLabel{
                font-size: 120px;
                background-color: #979da6;
                border-radius: 30px;
            }
                           """)
        
#Here we connect the actions to the buttons in this case when we click, using the clicked method
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.restart_button.clicked.connect(self.restart)
        self.timer.timeout.connect(self.update_display)

    def start(self): #Sends the signal to start
        self.timer.start(10) #This set an interval for time out every "10" miliseconds, that is what we declare

    def stop(self): #Sends the signal to stop
        self.timer.stop()

    def restart(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time): #Here we pass a time that has been already declare and give them the properties of hours, minutes, seconds and milliseconds to show that way
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10 #The // 10 is to dived by ten and only get 2 digits
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self): #We update the timer every 10 milliseconds
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
    