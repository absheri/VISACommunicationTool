import sys
import socket
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class IpConnectionC(QDialog):

    def __init__(self, parent=None, device=None):
        super(IpConnectionC,self).__init__(parent)
        self.setFixedSize(500,500)
        self.device = device
        self.listIp = ['', '']
        #
        self.ipLabal1 = QLabel(self)
        self.ipLabal1.setText("IP:")
        self.ipLabal1.move(25, 25)
        self.ipLabal2 = QLabel(self)
        #self.ipLabal2.setText("Scan List:" + '\n')
        self.listIp[0] = "Scan List:"
        #self.ipLabal2.move(25, 75)
        self.ipLabal2.setGeometry(25, 75, 400, 50)
        self.ipLabal3 = QLabel(self)
        # self.ipLabal2.setText("Scan List:" + '\n')
        #self.listIp[0] = "Scan List:"
        # self.ipLabal2.move(25, 75)
        self.ipLabal3.setGeometry(25, 125, 400, 50)
        #
        self.portLabal= QLabel(self)
        self.portLabal.setText("Port:")
        self.portLabal.move(225, 25)
        #
        self.ipInput = QLineEdit(self)
        self.ipInput.setGeometry(50, 20, 150, 25)
        #
        self.portInput = QLineEdit(self)
        self.portInput.setGeometry(250, 20, 50, 25)
        #
        self.buttonConnect = QPushButton(self)
        self.buttonConnect.move(315, 22)
        self.buttonConnect.setText("IP Connection")
        #
        self.buttonScan = QPushButton(self)
        self.buttonScan.move(25, 50)
        self.buttonScan.setText("IP Scan")
        #
        self.setWindowTitle("IP Connection")

        self.buttonConnect.clicked.connect(self.ipConnectD)
        self.buttonScan.clicked.connect(self.ipScanD)

    def ipScanD(self):
        localIP = socket.gethostbyname(socket.gethostname())
        #self.ipLabal2.setText("local ip:%s " % localIP)
        #self.listIp[0] = ("Local IP:%s " % localIP)
        #print("local ip:%s " % localIP)
        ipList = socket.gethostbyname_ex(socket.gethostname())
        for i in ipList:
            if i != localIP:
                self.listIp[1] = self.listIp[1] + '\n' + ("external IP:%s" % i)
        self.ipLabal2.setText("Local IP:%s " % localIP)
        self.ipLabal3.setText(self.listIp[1])

    def ipConnectD(self):
        HOST = self.ipInput.text()
        PORT = self.portInput.text()
        #HOST = "192.168.1.1"
        #PORT = 0000

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))