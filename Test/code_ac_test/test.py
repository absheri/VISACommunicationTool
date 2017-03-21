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
        self.connected_device = None

    def init_main(self):
        self.setGeometry(600,600,800,600)
        self.setWindowTitle('VISA Communication')
        self.setWindowIcon(QIcon('..\..\Src\Img\icon.png'))
        self.idn_connected_device()
        self.show()

    def idn_connected_device(self):
        self.connected_device = "AWG1224"

    def active_extention(self):
        self.extention = CodeAC(self.entry, self.connected_device)
        self.extention.active_script()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = MainWindow()
    root.init_main()
    root.active_extention()
    sys.exit(app.exec_())
