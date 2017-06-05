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

###All the def name with last letter 'D'; All the class name with last letter 'C'

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        #MenuBar
        self.statusBar()
        self.menu_bar = self.menuBar()
        #Display the devive model
        self.ipInformationDisplay = QLabel(self)
        self.ipInformationDisplay.setText('IP:__________   Hostname:__________   Model: ')
        self.modelDisplay = QLabel(self)
        #Command input area
        self.textInput = QLineEdit(self)
        self.textInput.setFixedWidth(500)
        #Command output area with scroll
        self.labelOutput = QLabel(self)
        self.main_widget = QWidget(self)
        self.scrollArea = QScrollArea(self.main_widget)
        self.main_widget.setGeometry(25, 100, 775, 325)
        self.main_widget.setStyleSheet("background-color: lightgray")
        self.scrollArea.setWidget(self.labelOutput)
        self.scrollArea.setWidgetResizable(True)
        self.layout = QVBoxLayout(self.main_widget)
        self.layout.addWidget(self.scrollArea)
        #self.scrollArea.verticalScrollBar().setValue(self.scrollArea.verticalScrollBar().max())
        #Three functions button
        self.buttonWrite = QPushButton(self)
        self.buttonQuery = QPushButton(self)
        self.buttonHistory = QPushButton(self)
        #IP connection
        self.ipLabal1 = QLabel(self)
        self.ipInput = QLineEdit(self)
        self.combo = QComboBox(self)
        self.combo.addItem("192.168.1.1")
        self.buttonConnect = QPushButton(self)
        #Combo of history command
        self.historyCombo = QComboBox(self)
        #History
        self.list = ['', '', '', '', '', '1'] #Seperate the output
        self.historysign = 0 #Number of history command to check history got 25 or not
        self.buttonUp = QPushButton(self)
        self.buttonDown = QPushButton(self)
        self.listCommand = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''] #Homepage command history
        self.commandSign = 0 #Check command history current
        self.currPos = 0 #Count history command
        #
        self.commands_from_files = []
        ###
        self.file_io = QFileDialog()
        self.connected_device = "No Device"
        self.extention = None
        self.query_window = None
        self.communication = None

    def init_main(self):
        #Main Window
        self.setGeometry(100, 100, 825, 600)
        self.setWindowTitle("Tektronix VISA Communicate Tool")
        self.setWindowIcon(QIcon('../Img/icon.png'))
        ###Menubar
        #File
        fileMenu = self.menu_bar.addMenu('&File')
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)
        #Edit
        editMenu = self.menu_bar.addMenu('&Edit')
        editMenu.addAction("...")

        #connectionMenu = self.menu_bar.addMenu('&Connection')
        #connectAction = QAction('&Connect', self)
        #connectAction.triggered.connect(self.ipConnectionD)
        #connectionMenu.addAction(connectAction)
        #Setting
        settingMenu = self.menu_bar.addMenu('&Setting')
        settingMenu.addAction("...")
        #Help
        helpMenu = self.menu_bar.addMenu('&Help')
        helpMenu.addAction("...")
        #Tool
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
        self.ipLabal1.setText("IP:")
        self.ipLabal1.move(25, 55)
        self.ipInput.setGeometry(50, 60, 200, 25)
        self.combo.move(350, 55)
        self.buttonConnect.move(500, 55)
        self.buttonConnect.setText("IP Connection")
        self.buttonConnect.clicked.connect(self.set_current_device)
        #
        self.textInput.move(25, 480)
        #
        self.historyCombo.setGeometry(25, 520, 500, 25)
        self.historyCombo.activated.connect(self.commandHistoryD)
        #
        self.labelOutput.setGeometry(25, 75, 200, 120)
        self.labelOutput.adjustSize()
        self.labelOutput.setWordWrap(True)
        self.labelOutput.setAlignment(QtCore.Qt.AlignTop)

        #self.labelOutput.s
        #
        self.buttonWrite.setText("Write")  # text
        self.buttonWrite.setIcon(QIcon("../Img/Write Icon.png"))
        self.buttonWrite.clicked.connect(self.writeSendD)
        self.buttonWrite.setGeometry(560, 460, 75, 75)
        self.buttonWrite.setObjectName("ButtonWrite")
        self.buttonWrite.setShortcut('Ctrl+W')  # shortcut key
        #
        self.buttonQuery.setText("Query")  # text
        self.buttonQuery.setIcon(QIcon("../Img/Query Icon.png"))
        self.buttonQuery.clicked.connect(self.querySendD)
        self.buttonQuery.setGeometry(640, 460, 75, 75)
        self.buttonQuery.setObjectName("ButtonQuery")
        self.buttonQuery.setShortcut('Ctrl+Q')  # shortcut key
        #
        self.buttonHistory.setText("History")  # text
        self.buttonHistory.setIcon(QIcon("../Img/History Icon.png"))
        self.buttonHistory.clicked.connect(self.active_history)
        self.buttonHistory.setGeometry(720, 460, 75, 75)
        self.buttonHistory.setObjectName("ButtonHistory")
        self.buttonHistory.setShortcut('Ctrl+H')  # shortcut key
        #Last command of history
        self.buttonUp.setText("↑")  # text
        self.buttonUp.clicked.connect(self.commandPrevD)
        self.buttonUp.setGeometry(530, 470, 25, 25)
        self.buttonUp.setObjectName("Prev Command")
        self.buttonUp.setShortcut('Ctrl+Z')  # shortcut key
        #Next command of history
        self.buttonDown.setText("↓")  # text
        self.buttonDown.clicked.connect(self.commandNextD)
        self.buttonDown.setGeometry(530, 500, 25, 25)
        self.buttonDown.setObjectName("Next Command")
        self.buttonDown.setShortcut('Ctrl+SHIFT+Z')  # shortcut key
        #Can't use as no prev and next command
        if self.currPos == 0:
            self.buttonUp.setEnabled(False)
            self.buttonDown.setEnabled(False)
        #
        self.show()

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

    def active_extention(self):
        self.extention = CodeAC(self.textInput, self.connected_device)
        self.extention.active_script()

    def active_query(self):
        print(self.connected_device)
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

            send_command = self.communication.write_to_device(currInput)
        except:
            print('INTR Error: No device detected')

        # self.labelOutput.adjustSize()
        #command prev and next
        self.commandSign = self.currPos
        self.buttonUp.setEnabled(True) #Can use the UP button as has at least one command in the history
        self.buttonDown.setEnabled(False)
        #The history is not full with 25 commands
        if self.currPos != 25:
            self.listCommand[self.currPos] = currInput
            self.historyCombo.addItem(self.listCommand[self.currPos])
            self.currPos += 1
            self.commandSign = self.currPos
        #The history is full with 25 commands
        else:
            for i in range(0, 24):
                self.listCommand[i] = self.listCommand[i + 1]
            self.listCommand[24] = currInput
            self.historyCombo.addItem(self.listCommand[24])
        #history
        #The history is not full with 25 commands
        if self.historysign != 25:
            listHistory[self.historysign] = self.currtime + ' ~   ' + signal + currInput
            self.historysign += 1
        #The history is full with 25 commands
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
            query_result = self.communication.query_from_device(currInput)
            currOutput = self.list[0] + '\n' + query_result
            self.list[0] = currOutput
            self.labelOutput.setText(currOutput)
            #print(query_result)
        except:
            currOutput = self.list[0] + '\n' + 'INTR Error: No device detected' + '\n'
            self.list[0] = currOutput
            self.labelOutput.setText(currOutput)
        #command prev and next
        self.commandSign = self.currPos
        self.buttonUp.setEnabled(True)
        self.buttonDown.setEnabled(False)
        #The history is not full with 25 commands
        if self.currPos != 25:
            self.listCommand[self.currPos] = currInput
            self.historyCombo.addItem(self.listCommand[self.currPos])
            self.currPos += 1
            self.commandSign = self.currPos
        #The history is full with 25 commands
        else:
            for i in range(0, 24):
                self.listCommand[i] = self.listCommand[i + 1]
            self.listCommand[24] = currInput
            self.historyCombo.addItem(self.listCommand[24])
        #history
        #The history is not full with 25 commands
        if self.historysign != 25:
            listHistory[self.historysign] = self.currtime + ' ~   ' + signal + currInput
            self.historysign += 1
        #The history is full with 25 commands
        else:
            for i in range(0, 24):
                listHistory[i] = listHistory[i + 1]
            listHistory[24] = self.currtime + ' ~   ' + signal + currInput
        #
        self.textInput.setText('')

    #Function for Sub-window of command history
    def active_history(self):
        self.history_window = HistoryC(self, self.connected_device)
        self.history_window.setGeometry(100, 200, 400, 400)
        self.history_window.show()

    #Funnction of IP with sub-window(Not use now)
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

    def commandHistoryD(self):
        self.textInput.setText(self.historyCombo.currentText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    VCT = Window()
    #VCT.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
    VCT.init_main()
    #VCT.set_communication()
    # Need an inner function call to set the current device
    sys.exit(app.exec_())

