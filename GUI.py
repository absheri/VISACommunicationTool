import sys
import socket
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
'''
def window():
    app = QtWidgets.QApplication(sys.argv)
    VCT = QtWidgets.QWidget()
    new = QtWidgets.QWidget()
    VCT.resize(400, 400)
    VCT.setWindowTitle("Tektronix VISA Communicate Tool")
    l1 = QLabel(VCT)
    l1.move(100, 100)
    l1.setText('123')
    VCT.show()
    sys.exit(app.exec_())


window()
'''
app = QtWidgets.QApplication(sys.argv)
VCT = QtWidgets.QWidget()
new = QtWidgets.QWidget()
VCT.resize(400, 400)
VCT.setWindowTitle("Tektronix VISA Communicate Tool")
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
enter.move(100,250)
screen = QLabel(VCT)
screen.move(100,100)



list = ['','']
def send():
    str1 = 'W'

    stro = enter.text()

    str123 = list[0] + '\n' + str1 + stro
    list[0] = str123
   #print(stro)
    #print(str123)
    screen.setText(str123)
    #screen.append(str123)
    screen.adjustSize()

def qsend():
    str1 = 'Q'

    stro = enter.text()

    str123 = list[0] + '\n' + str1 + stro
    list[0] = str123
   #print(stro)
    #print(str123)
    screen.setText(str123)
    #screen.append(str123)
    screen.adjustSize()

###write
buttonwrite = QtWidgets.QPushButton(VCT)
buttonwrite.setText("write")          #text
#buttonwrite.setIcon(QIcon("close.png")) #icon
#buttonwrite.setShortcut('Ctrl+D')  #shortcut key
buttonwrite.clicked.connect(send)
#buttonwrite.setToolTip("Get help") #Tool tip
buttonwrite.move(300,200)
buttonwrite.setObjectName("buttonwrite")

###qurey
buttonqurey = QtWidgets.QPushButton(VCT)
buttonqurey.setText("qurey")          #text
#buttonwrite.setIcon(QIcon("close.png")) #icon
#buttonwrite.setShortcut('Ctrl+D')  #shortcut key
buttonqurey.clicked.connect(qsend)
#buttonwrite.setToolTip("Get help") #Tool tip
buttonqurey.move(300,225)
buttonqurey.setObjectName("buttonqurey")

localIP = socket.gethostbyname(socket.gethostname())
print("local ip:%s "%localIP)
ipList = socket.gethostbyname_ex(socket.gethostname())
for i in ipList:
    if i != localIP:
       print("external IP:%s"%i)

VCT.show()
sys.exit(app.exec_())


window()

