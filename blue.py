import sys
import time
import os

from PyQt5 import QtGui, QtCore, uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap

start_time = time.time()
class App(QWidget):
    
    def __init__(self):
        super().__init__()
        self.title = 'Blue'
        self.screen = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.left = 1
        self.top = -1000
        self.width = 0
        self.height = 0
        self.initUI()
    

    
    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # # Create widget
        label = QLabel(self)
        pixmap = QPixmap('blue.png')
        label.setPixmap(pixmap)
        self.resize(100,100)
        self.show()
   

        
 
# # This is a countdown, now after the countdown blue appears on sceeen
# # define the countdown func.
# def countdown(t):
	
# 	while t:
# 		mins, secs = divmod(t, 60)
# 		timer = '{:02d}:{:02d}'.format(mins, secs)
# 		print(timer, end="\r")
# 		time.sleep(1)
# 		t -= 1
	
# 	print('Hi Blueee')


# # input time in seconds
# t = input("Enter the time in seconds: ")

# # function call
# countdown(int(t))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
e = int(time.time() - start_time)
print('{:02d}:{:02d}:{:02d}'.format(e // 3600, (e % 3600 // 60), e % 60))