import sys
from Src.Extention.src.code_ac import *
import ctypes


MyAppID = 'Tektronix.VISA.Communication.v1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(MyAppID)


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.statusBar()
        self.menu_bar = self.menuBar()
        self.ipInformationDisplay = QLabel(self)
        self.textInput = QLineEdit(self)
        self.textInput.setFixedWidth(500)
        self.labelOutput = QLabel(self)
        self.buttonWrite = QPushButton(self)
        self.buttonQuery = QPushButton(self)
        self.list = ['', '']
        ###
        self.connected_device = None
        self.extention = None
        self.query_window = None

    def init_main(self):
        self.setGeometry(600, 600, 800, 600)
        self.setWindowTitle("Tektronix VISA Communicate Tool")
        self.setWindowIcon(QIcon('../Img/icon.png'))
        #
        fileMenu = self.menu_bar.addMenu('&File')
        exitAction = QAction('&Exit', self)
        exitAction.triggered.connect(self.close)
        fileMenu.addAction(exitAction)

        editMenu = self.menu_bar.addMenu('&Edit')
        editMenu.addAction("123")

        settingMenu = self.menu_bar.addMenu('&Setting')
        settingMenu.addAction("123")

        helpMenu = self.menu_bar.addMenu('&Help')
        helpMenu.addAction("123")
        #
        ToolMenu = self.menu_bar.addMenu('&Tool')
        QueryAction = QAction('&Query', self)
        QueryAction.triggered.connect(self.active_query)
        ToolMenu.addAction(QueryAction)
        #
        self.ipInformationDisplay.move(25, 25)
        #
        self.textInput.move(25, 450)

        self.labelOutput.setGeometry(25, 75, 200, 120)
        #
        self.buttonWrite.setText("Write")  # text
        self.buttonWrite.clicked.connect(self.writeSendD)
        self.buttonWrite.move(600, 450)
        self.buttonWrite.setObjectName("ButtonWrite")
        self.buttonWrite.setShortcut('Ctrl+W')  # shortcut key
        #
        self.buttonQuery.setText("Query")  # text
        self.buttonQuery.clicked.connect(self.active_query)
        self.buttonQuery.move(600, 475)
        self.buttonQuery.setObjectName("ButtonQuery")
        self.buttonQuery.setShortcut('Ctrl+Q')  # shortcut key
        #
        self.show()

    def idn_connected_device(self):
        self.connected_device = "AWG1224"

    def active_extention(self):
        self.extention = CodeAC(self.textInput, self.connected_device)
        self.extention.active_script()

    def active_query(self):
        self.query_window = DocQuery(self, self.connected_device)
        self.query_window.setGeometry(100, 200, 400, 400)
        self.query_window.show()

    def writeSendD(self):
        signal = 'W->'
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + signal + currInput
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        self.labelOutput.adjustSize()

    def querySendD(self):
        signal = 'Q->'
        currInput = self.textInput.text()
        currOutput = self.list[0] + '\n' + signal + currInput
        self.list[0] = currOutput
        self.labelOutput.setText(currOutput)
        self.labelOutput.adjustSize()


if __name__=="__main__":
    app = QApplication(sys.argv)
    VCT = Window()
    VCT.init_main()
    VCT.idn_connected_device()
    VCT.active_extention()
    sys.exit(app.exec_())

