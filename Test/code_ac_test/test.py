from Src.Extention.src.code_ac import *
import sys
import ctypes


MyAppID = 'Tektronix.VISA.Communication.v1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(MyAppID)


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.extention = None
        self.entry = QLineEdit(self)
        self.entry.setFixedWidth(100)
        self.connected_device = None
        self.query_window = None
        self.btn1 = QPushButton("Button 1", self)
        self.btn1.move(150, 50)

    def init_main(self):
        self.setGeometry(600,600,800,600)
        self.setWindowTitle('VISA Communication')
        self.setWindowIcon(QIcon('..\..\Src\Img\icon.png'))
        self.btn1.clicked.connect(self.active_query)
        self.idn_connected_device()
        self.show()

    def idn_connected_device(self):
        self.connected_device = "AWG1224"

    def active_extention(self):
        self.extention = CodeAC(self.entry, self.connected_device)
        self.extention.active_script()

    def active_query(self):
        self.query_window = DocQuery(self)
        self.query_window.setGeometry(100, 200, 400, 400)
        self.query_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.init_main()
    root.active_extention()
    sys.exit(app.exec_())
