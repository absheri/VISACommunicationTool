import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Src.Main.GUI import *
class HistoryC(QDialog):

    def __init__(self, parent=None, device=None):
        super(HistoryC,self).__init__(parent)
        self.setFixedSize(500,500)
        self.device = device
        #
        self.historyLabal = QLabel(self)
        self.historyLabal.setText(listHistory[0] + '\n' + listHistory[1] + '\n' + listHistory[2] + '\n' + listHistory[3] + '\n' + listHistory[4] + '\n' + listHistory[5] + '\n' + listHistory[6] + '\n' + listHistory[7] + '\n' + listHistory[8] + '\n' + listHistory[9] + '\n' + listHistory[10] + '\n' + listHistory[11] + '\n' + listHistory[12] + '\n' + listHistory[13] +'\n' + listHistory[14] + '\n' + listHistory[15] + '\n' + listHistory[16] +'\n' + listHistory[17] + '\n' + listHistory[18] + '\n' + listHistory[19] +'\n' + listHistory[20] + '\n' + listHistory[21] + '\n' + listHistory[22] + '\n' + listHistory[23] + '\n' + listHistory[24])
        self.historyLabal.setGeometry(25, 25, 400, 400)


        self.setWindowTitle("Command History")


listHistory = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']