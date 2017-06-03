import sys
import ctypes
import datetime

from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from Src.Extention.src.IPconnection import *
from Src.Extention.src.code_ac import *
from Src.Extention.src.communication import *
from Src.Extention.src.history import *

MyAppID = 'Tektronix.VISA.Communication.v1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(MyAppID)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar()
        self.menu_bar = self.menuBar()
        self.ipInformationDisplay = QLabel(self)
        self.ipInformationDisplay.setText('IP:__________   Hostname:__________   Model: ')
        self.modelDisplay = QLabel(self)
        self.textInput = QLineEdit(self)
        self.textInput.setFixedWidth(500)
        self.labelOutput = QLabel(self)
        self.main_widget = QWidget(self)
        self.scrollArea = QScrollArea(self.main_widget)
<<<<<<< HEAD
        self.main_widget.setGeometry(25, 75, 775, 325)
=======
        self.main_widget.setGeometry(25, 100, 775, 325)
        self.main_widget.setStyleSheet("background-color: lightgray")
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.scrollArea.setWidget(self.labelOutput)
        self.scrollArea.setWidgetResizable(True)
        self.layout = QVBoxLayout(self.main_widget)
        self.layout.addWidget(self.scrollArea)
        self.buttonWrite = QPushButton(self)
        self.buttonQuery = QPushButton(self)
        self.buttonHistory = QPushButton(self)
<<<<<<< HEAD
=======
        #
        self.ipLabal1 = QLabel(self)
        self.ipInput = QLineEdit(self)
        self.combo = QComboBox(self)
        self.combo.addItem("192.168.1.1")
        self.buttonConnect = QPushButton(self)
        #
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.list = ['', '', '', '', '', '1']
        self.historysign = 0
        self.buttonUp = QPushButton(self)
        self.buttonDown = QPushButton(self)
        self.listCommand = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
        self.commandSign = 0
        self.currPos = 0
<<<<<<< HEAD
        ###
        self.file_io = QFileDialog()
        self.connected_device = None
        self.extention = None
        self.query_window = None
        self.commands_from_files = []

    def init_main(self):
        self.setGeometry(100, 100, 800, 600)
=======
        self.commands_from_files = []
        ###
        self.file_io = QFileDialog()
        self.connected_device = "No Device"
        self.extention = None
        self.query_window = None
        self.communication = None

    def init_main(self):
        self.setGeometry(100, 100, 825, 600)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.setWindowTitle("Tektronix VISA Communicate Tool")
        self.setWindowIcon(QIcon('../Img/icon.png'))
        #
        fileMenu = self.menu_bar.addMenu('&File')
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        editMenu = self.menu_bar.addMenu('&Edit')
        editMenu.addAction("...")

<<<<<<< HEAD
        connectionMenu = self.menu_bar.addMenu('&Connection')
        connectAction = QAction('&Connect', self)
        connectAction.triggered.connect(self.ipConnectionD)
        connectionMenu.addAction(connectAction)
=======
        #connectionMenu = self.menu_bar.addMenu('&Connection')
        #connectAction = QAction('&Connect', self)
        #connectAction.triggered.connect(self.ipConnectionD)
        #connectionMenu.addAction(connectAction)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12

        settingMenu = self.menu_bar.addMenu('&Setting')
        settingMenu.addAction("...")

        helpMenu = self.menu_bar.addMenu('&Help')
        helpMenu.addAction("...")
        #
        toolMenu = self.menu_bar.addMenu('&Tool')
        QueryAction = QAction('&Query', self)
        QueryAction.triggered.connect(self.active_query)
        toolMenu.addAction(QueryAction)
        importAction = QAction('&Import', self)
        importAction.triggered.connect(self.read_from_file)
        toolMenu.addAction(importAction)
        #
        self.ipInformationDisplay.setGeometry(25, 25, 500, 25)
        #
        self.modelDisplay.setGeometry(270,32,500,25)
        #
<<<<<<< HEAD
        self.textInput.move(25, 450)
=======
        self.ipLabal1.setText("IP:")
        self.ipLabal1.move(25, 55)
        self.ipInput.setGeometry(50, 60, 200, 25)
        self.combo.move(350, 55)
        self.buttonConnect.move(500, 55)
        self.buttonConnect.setText("IP Connection")
        self.buttonConnect.clicked.connect(self.set_current_device)
        #
        self.textInput.move(25, 480)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12

        self.labelOutput.setGeometry(25, 75, 200, 120)
        #
        self.buttonWrite.setText("Write")  # text
<<<<<<< HEAD
        self.buttonWrite.clicked.connect(self.writeSendD)
        self.buttonWrite.move(600, 450)
=======
        self.buttonWrite.setIcon(QIcon("../Img/Write Icon.png"))
        self.buttonWrite.clicked.connect(self.writeSendD)
        self.buttonWrite.setGeometry(560, 460, 75, 75)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.buttonWrite.setObjectName("ButtonWrite")
        self.buttonWrite.setShortcut('Ctrl+W')  # shortcut key
        #
        self.buttonQuery.setText("Query")  # text
<<<<<<< HEAD
        self.buttonQuery.clicked.connect(self.querySendD)
        self.buttonQuery.move(600, 480)
=======
        self.buttonQuery.setIcon(QIcon("../Img/Query Icon.png"))
        self.buttonQuery.clicked.connect(self.querySendD)
        self.buttonQuery.setGeometry(640, 460, 75, 75)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.buttonQuery.setObjectName("ButtonQuery")
        self.buttonQuery.setShortcut('Ctrl+Q')  # shortcut key
        #
        self.buttonHistory.setText("History")  # text
<<<<<<< HEAD
        self.buttonHistory.clicked.connect(self.active_history)
        self.buttonHistory.move(700, 465)
=======
        self.buttonHistory.setIcon(QIcon("../Img/History Icon.png"))
        self.buttonHistory.clicked.connect(self.active_history)
        self.buttonHistory.setGeometry(720, 460, 75, 75)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.buttonHistory.setObjectName("ButtonHistory")
        self.buttonHistory.setShortcut('Ctrl+H')  # shortcut key
        #
        self.buttonUp.setText("↑")  # text
        self.buttonUp.clicked.connect(self.commandPrevD)
<<<<<<< HEAD
        self.buttonUp.setGeometry(530, 440, 25, 25)
=======
        self.buttonUp.setGeometry(530, 470, 25, 25)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.buttonUp.setObjectName("Prev Command")
        self.buttonUp.setShortcut('Ctrl+Z')  # shortcut key
       #
        self.buttonDown.setText("↓")  # text
        self.buttonDown.clicked.connect(self.commandNextD)
<<<<<<< HEAD
        self.buttonDown.setGeometry(530, 470, 25, 25)
=======
        self.buttonDown.setGeometry(530, 500, 25, 25)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.buttonDown.setObjectName("Next Command")
        self.buttonDown.setShortcut('Ctrl+SHIFT+Z')  # shortcut key
        #can't use as no prev command
        if self.currPos == 0:
            self.buttonUp.setEnabled(False)
            self.buttonDown.setEnabled(False)
        #
        self.show()

<<<<<<< HEAD
    def idn_connected_device(self):
        try:
            temp_com = CommunicationInterface()
            self.connected_device = temp_com.device_identification()
        except:
            self.connected_device = "AWG1224"
        self.modelDisplay.setText(self.connected_device)
        print (self.connected_device)
=======
    def set_communication(self):
        try:
            self.communication = CommunicationInterface()
        except:
            print('No NI-VISA')

    def set_current_device(self):
        try:
            ip_address = self.ipInput.text()
        except:
            ip_address = None
        # After entering IP address, the communication will set up
        if ip_address is not None:
            try:
                self.connected_device = self.communication.set_current_device(ip_address)
            except:
                print('communication initial error')
        self.modelDisplay.setText(self.connected_device)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12

    def active_extention(self):
        self.extention = CodeAC(self.textInput, self.connected_device)
        self.extention.active_script()

    def active_query(self):
<<<<<<< HEAD
=======
        print(self.connected_device)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        self.query_window = DocQuery(self, self.connected_device)
        self.query_window.setGeometry(100, 200, 400, 400)
        self.query_window.show()

    def read_from_file(self):
        file = self.file_io.getOpenFileName(self, 'Open file')
        if file[0]:
            f = open(file[0], 'r')
            if f is not None:
                for row in f:
                    if row is not None:
                        self.commands_from_files.append(row)

    def writeSendD(self):
        self.currtime = datetime.datetime.now().strftime('%H:%M:%S')
        signal = ' W->   '
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + self.currtime + ' ~   ' + signal + currInput + '\n'
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        #
        try:
<<<<<<< HEAD
            communication_driver = CommunicationInterface()
            send_command = communication_driver.write_to_device(currInput)
=======

            send_command = self.communication.write_to_device(currInput)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
        except:
            print('INTR Error: No device detected')

        # self.labelOutput.adjustSize()
        #command prev and next
        self.commandSign = self.currPos
        self.buttonUp.setEnabled(True)
        self.buttonDown.setEnabled(False)
        if self.currPos != 25:
            self.listCommand[self.currPos] = currInput
            self.currPos += 1
            self.commandSign = self.currPos
        else:
            for i in range(0, 24):
                self.listCommand[i] = self.listCommand[i + 1]
            self.listCommand[24] = currInput
        #history
        if self.historysign != 25:
            listHistory[self.historysign] = self.currtime + ' ~   ' + signal + currInput
            self.historysign += 1
        else:
            for i in range(0, 24):
                listHistory[i] = listHistory[i + 1]
            listHistory[24] = self.currtime + ' ~   ' + signal + currInput
        #
        self.textInput.setText('')

    def querySendD(self):
        self.currtime = datetime.datetime.now().strftime('%H:%M:%S')
        signal = ' Q->   '
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + self.currtime + ' ~   ' + signal + currInput
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        #self.labelOutput.adjustSize()
        #
        try:
<<<<<<< HEAD
            communication_driver = CommunicationInterface()
            '''
                query --> result queried from device
            '''
            query_result = communication_driver.query_from_device(currInput)
=======
            query_result = self.communication.query_from_device(currInput)
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
            currOutput = self.list[0] + '\n' + query_result
            self.list[0] = currOutput
            self.labelOutput.setText(currOutput)
            #print(query_result)
        except:
<<<<<<< HEAD
            print('INTR Error: No device detected')
=======
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
            currOutput = self.list[0] + '\n' + 'INTR Error: No device detected' + '\n'
            self.list[0] = currOutput
            self.labelOutput.setText(currOutput)
        #command prev and next
        self.commandSign = self.currPos
        self.buttonUp.setEnabled(True)
        self.buttonDown.setEnabled(False)
        if self.currPos != 25:
            self.listCommand[self.currPos] = currInput
            self.currPos += 1
            self.commandSign = self.currPos
        else:
            for i in range(0, 24):
                self.listCommand[i] = self.listCommand[i + 1]
            self.listCommand[24] = currInput
        #history
        if self.historysign != 25:
            listHistory[self.historysign] = self.currtime + ' ~   ' + signal + currInput
            self.historysign += 1
        else:
            for i in range(0, 24):
                listHistory[i] = listHistory[i + 1]
            listHistory[24] = self.currtime + ' ~   ' + signal + currInput
        #
        self.textInput.setText('')

    def active_history(self):
        self.history_window = HistoryC(self, self.connected_device)
        self.history_window.setGeometry(100, 200, 400, 400)
        self.history_window.show()

    def ipConnectionD(self):
        self.ip_window = IpConnectionC(self, self.connected_device)
        self.ip_window.setGeometry(100, 200, 400, 400)
        self.ip_window.show()

    def commandPrevD(self):
        if self.commandSign != 0:
           self.commandSign -= 1
           self.textInput.setText(self.listCommand[self.commandSign])
           self.buttonDown.setEnabled(True)
           if self.commandSign == 0:
               self.buttonUp.setEnabled(False)
        else:
            self.buttonUp.setEnabled(False)

    def commandNextD(self):
        if (self.commandSign != 25) or (self.commandSign != 24):
           self.commandSign += 1
           self.textInput.setText(self.listCommand[self.commandSign])
           self.buttonUp.setEnabled(True)
           if (self.commandSign == 24) or (self.listCommand[self.commandSign] == ''):
               self.buttonDown.setEnabled(False)
        else:
            self.buttonUp.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    VCT = Window()
<<<<<<< HEAD
    VCT.init_main()
    VCT.idn_connected_device()
    VCT.active_extention()
=======
    #VCT.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    VCT.init_main()
    #VCT.set_communication()
    # Need an inner function call to set the current device
>>>>>>> 77070586f8121a9a70f01eec5e98616f36649c12
    sys.exit(app.exec_())

