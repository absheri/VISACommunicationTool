from Src.Extention.src.code_ac import *
import sys
import ctypes


MyAppID = 'Tektronix.VISA.Communication.v1.0'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(MyAppID)


class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.extention = None
        self.init_main()

    def init_main(self):
        self.setGeometry(600,600,800,600)
        self.setWindowTitle('VISA Communication')
        self.setWindowIcon(QIcon('..\..\Src\Img\icon.png'))
        self.extention = CodeAC(self)
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    root = MainWindow()
    sys.exit(app.exec_())
