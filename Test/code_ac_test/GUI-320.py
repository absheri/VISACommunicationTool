#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.windowD()
    def windowD(self):
        self.resize(400, 400)
        self.setWindowTitle("Tektronix VISA Communicate Tool")
        self.setWindowIcon(QIcon('Tekicon.png'))

        self.menuBarD()
        self.ipInformationDisplayD()
        self.textInputD()
        self.labelOutputD()
        self.buttonWriteD()
        self.buttonQueryD()
        self.list = ['', '']
        self.show()

    def menuBarD(self):
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        editMenu = menubar.addMenu('&Edit')
        #exitAction = QAction('&Exit', self)
        #exitAction.triggered.connect(self.close)
        editMenu.addAction("123")

        connectionMenu = menubar.addMenu('&Connection')
        connectAction = QAction('&Connect', self)
        connectAction.triggered.connect(self.ipNewWindowD)
        connectionMenu.addAction(connectAction)

        settingMenu = menubar.addMenu('&Setting')
        # exitAction = QAction('&Exit', self)
        # exitAction.triggered.connect(self.close)
        settingMenu.addAction("123")

        helpMenu = menubar.addMenu('&Help')
        # exitAction = QAction('&Exit', self)
        # exitAction.triggered.connect(self.close)
        helpMenu.addAction("123")

    def ipInformationDisplayD(self):
        self.ipInformationDisplay = QLabel(self)
        self.ipInformationDisplay.move(25, 25)
        #self.ipInformationDisplay.setText('IP:__________   Hostname:__________   Model:__________')
        self.ipInformationDisplay.setText('IP_Hostname_Model_   ')
    def ipNewWindowD(self):
        new = QtWidgets.QWidget()
        new.resize(300, 300)  # set the size
        new.setWindowTitle("Tektronix VISA Communicate Tool")
        new.setWindowIcon(QIcon('Tekicon.png'))
        new.show()

    def textInputD(self):
        self.textInput = QLineEdit(self)
        self.textInput.move(25, 250)
    def labelOutputD(self):
        self.labelOutput = QLabel(self)
        self.labelOutput.move(25, 75)
        self.labelOutput.setGeometry(25, 75, 200, 120) #(x,y,w,h)

        ###labelOutput.setText('123')
    def buttonWriteD(self):
        buttonWrite = QPushButton(self)
        buttonWrite.setText("Write")    # text
        buttonWrite.clicked.connect(self.writeSendD)
        buttonWrite.move(300, 250)
        buttonWrite.setObjectName("ButtonWrite")
        buttonWrite.setShortcut('Ctrl+W')  #shortcut key
    def writeSendD(self):
        signal = 'W->'
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + signal + currInput
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        self.labelOutput.adjustSize()
    def buttonQueryD(self):
        buttonQuery = QPushButton(self)
        buttonQuery.setText("Query")    # text
        buttonQuery.clicked.connect(self.querySendD)
        buttonQuery.move(300, 275)
        buttonQuery.setObjectName("ButtonQuery")
        buttonQuery.setShortcut('Ctrl+Q')  # shortcut key
    def querySendD(self):
        signal = 'Q->'
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + signal + currInput
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        self.labelOutput.adjustSize()
'''
class New(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ipNewWindowD()
    def ipNewWindowD(self):
        self.resize(300, 300)  # set the size
        self.setWindowTitle("Tektronix VISA Communicate Tool")
        self.setWindowIcon(QIcon('Tekicon.png'))
        self.show()
'''
       # new.setWindowTitle("IP Connection")  # name of the windows
app = QApplication(sys.argv)
VCT = Window()
#new = New()
sys.exit(app.exec_())

'''
app = QtWidgets.QApplication(sys.argv)
VCT = QtWidgets.QWidget()
new = QtWidgets.QWidget()
VCT.resize(400, 400)
VCT.setWindowTitle("Tektronix VISA Communicate Tool")
new = QtWidgets.QWidget() #create new windows
new.resize(300,300) # set the size
new.setWindowTitle("IP Connection") # name of the windows
###111111111111111111
button1 = QtWidgets.QPushButton(VCT)
button1.setText("File")          #text
#button1.setIcon(QIcon("close.png")) #icon
#button1.setShortcut('Ctrl+D')  #shortcut key
#button1.clicked.connect(self.close)
button1.setToolTip("Open the file") #Tool tip
#button1.move(100,100)
button1.setObjectName("button1")

###222222222222222222222222222
button2 = QtWidgets.QPushButton(VCT)
button2.setText("Edit")          #text
#button2.setIcon(QIcon("close.png")) #icon
#button2.setShortcut('Ctrl+D')  #shortcut key
#button2.clicked.connect(self.close)
button2.setToolTip("Edit") #Tool tip
button2.move(75,0)
button2.setObjectName("button2")

###3333333333333333333333
button3 = QtWidgets.QPushButton(VCT)
button3.setText("Connection")          #text
#button3.setIcon(QIcon("close.png")) #icon
#button3.setShortcut('Ctrl+D')  #shortcut key
def newwindow():

    new.resize(100, 100)
    new.show()
button3.clicked.connect(newwindow)

button3.setToolTip("Connect any device") #Tool tip
button3.move(150,0)
button3.setObjectName("button3")

###44444444444444444444444444
button4 = QtWidgets.QPushButton(VCT)
button4.setText("Setting")          #text
#button4.setIcon(QIcon("close.png")) #icon
#button4.setShortcut('Ctrl+D')  #shortcut key
#button4.clicked.connect(self.close)
button4.setToolTip("Setting anything") #Tool tip
button4.move(225,0)
button4.setObjectName("button4")

###55555555555555555555555555555
button5 = QtWidgets.QPushButton(VCT)
button5.setText("Help")          #text
#button5.setIcon(QIcon("close.png")) #icon
#button5.setShortcut('Ctrl+D')  #shortcut key
#button5.clicked.connect(self.close)
button5.setToolTip("Get help") #Tool tip
button5.move(300,0)
button5.setObjectName("button5")

enter = QLineEdit(VCT)
enter.move(25,250)
screen = QLabel(VCT)
screen.move(25,75)
ipenter = QLineEdit(new)
ipenter.move(25,50)


list = ['','']
def writesend():
    signal = 'W->'

    currinput = enter.text()

    curroutput = list[0] + '\n' + signal + currinput
    list[0] = curroutput
   #print(stro)
    #print(str123)
    screen.setText(curroutput)
    #screen.append(str123)
    screen.adjustSize()

def qureysend():
    signal = 'Q->'

    currinput = enter.text()

    curroutput = list[0] + '\n' + signal + currinput
    list[0] = curroutput
   #print(stro)
    #print(str123)
    screen.setText(curroutput)
    #screen.append(str123)
    screen.adjustSize()

def ipconnect():
    print("11111111111111111111111111111")

###write

buttonwrite = QtWidgets.QPushButton(VCT)
buttonwrite.setText("write")
buttonwrite.clicked.connect(writesend)
buttonwrite.move(300,250)
buttonwrite.setObjectName("buttonwrite")

#buttonwrite.setIcon(QIcon("close.png")) #icon
#buttonwrite.setShortcut('Ctrl+D')  #shortcut key
#buttonwrite.setToolTip("Get help") #Tool tip

###qurey
buttonqurey = QtWidgets.QPushButton(VCT)
buttonqurey.setText("qurey")          #text
#buttonwrite.setIcon(QIcon("close.png")) #icon
#buttonwrite.setShortcut('Ctrl+D')  #shortcut key
buttonqurey.clicked.connect(qureysend)
#buttonwrite.setToolTip("Get help") #Tool tip
buttonqurey.move(300,275)
buttonqurey.setObjectName("buttonqurey")

###ip connect
buttonip = QtWidgets.QPushButton(new)
buttonip.setText("ip connction")          #text
#buttonwrite.setIcon(QIcon("close.png")) #icon
#buttonwrite.setShortcut('Ctrl+D')  #shortcut key
buttonip.clicked.connect(ipconnect)
#buttonwrite.setToolTip("Get help") #Tool tip
buttonip.move(200,50)
buttonip.setObjectName("ip connction")


localIP = socket.gethostbyname(socket.gethostname())
print("local ip:%s "%localIP)
ipList = socket.gethostbyname_ex(socket.gethostname())
for i in ipList:
    if i != localIP:
       print("external IP:%s"%i)

VCT.show()
sys.exit(app.exec_())


window()

'''