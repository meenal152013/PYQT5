# -*- coding: utf-8 -*-
"""
Created on Tue Dec 29 15:08:00 2020

@author: khandelwal
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
'''Pyqt5 dynamically add and delete controls'''

class DynAddObject(QDialog):
    def __init__(self, parent=None):
        super(DynAddObject, self).__init__(parent)
        
        self.left = 500
        self.top = 200
        self.width = 1400
        self.height = 1200
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.widgetList = []
        addButton = QPushButton(u"+ Add NEW")
        self.layout = QGridLayout()
        self.layout.addWidget(addButton, 1, 4)
        self.setLayout(self.layout)
        addButton.clicked.connect(self.add)
        

    def add(self):
        btncont= self.layout.count()
        frame = QFrame( self)
        frame.resize(50,100)
        frame.setObjectName("FRAME")
        frame.setStyleSheet("background-color:white")
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setLineWidth(0.6)
        frame.heading =QLabel(frame)
        frame.heading.setText("MEETING AT 6:00 PM")
        frame.heading.move(70,10)
        frame.heading1 =QLabel(frame)
        frame.heading1.setText("20/10/2020")
        frame.heading1.move(10,70)
        frame.heading2 =QLabel(frame)
        frame.heading2.setText("4:35 PM")
        frame.heading2.move(200,70)
        frame.btn1 = QPushButton(frame)
        frame.btn1.setText("IMPORTANT")
        frame.btn1.setStyleSheet("background-color:#FBD2D7")
        frame.btn1.move(10,120)
        
        self.layout.addWidget(frame)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DynAddObject()
    form.show()
    app.exec_()