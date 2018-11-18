# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 17:38:02 2018

@author: karlh
"""

from PyQt5 import QtCore, QtGui, QtWidgets,uic
from PyQt5.QtWidgets import QDialog, QLabel, QApplication, QWidget
from PyQt5.QtGui import QIcon, QPixmap

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self) :
        super(MyWindow, self).__init__()
        uic.loadUi("Main_Window.ui",self)
        self.btn_Traffic.clicked.connect(self.execute_Traffic_Control)
        
    def execute_Traffic_Control(self):
        traffic_control = Traffic_Control()
        traffic_control.exec_()
        
        
        
        
class Traffic_Control(QDialog):
    def __init__(self):
        super(Traffic_Control,self).__init__()
        uic.loadUi("Traffic_Dialog.ui",self)
        self.getImage()
        self.getImage2()
        self.start_timer(self.timer_func(),5)
        self.btn_ok.clicked.connect(self.close)
        
    def getImage(self):
        image_path = "C:/Users/karlh/Documents/Hackathon/Traffic_Red.png"
        pixmap = QtGui.QPixmap(image_path)
        self.lbl_TrafficLight1.setPixmap(pixmap.scaled(80,130,QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))
        self.show()
        
    def getImage2(self):
        image_path = "C:/Users/karlh/Documents/Hackathon/Traffic_Green.png"
        pixmap = QtGui.QPixmap(image_path)
        self.lbl_TrafficLight2.setPixmap(pixmap.scaled(80,130,QtCore.Qt.KeepAspectRatio))
        self.show()
        
    def start_timer(slot, count=1, interval=1000):
        counter = 0
        def handler():
            nonlocal counter
            counter += 1
            slot(counter)
            if counter >= count:
                timer.stop()
                timer.deleteLater()
        timer = QtCore.QTimer()
        timer.timeout.connect(handler)
        timer.start(interval)
    
    def timer_func(count,self):
        self.txt_tl1.setText(count)
        if count >= 5:
            QtCore.QCoreApplication.quit()

         
if __name__ == '__main__' :
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
       