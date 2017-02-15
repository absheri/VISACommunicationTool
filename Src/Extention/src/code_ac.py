from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def get_data(model):

    #model.setStringList(["completion", "data", "goes", "here", "complain"])
    item = QStandardItem("test")
    item.setIcon(QIcon('..\..\Src\Img\O.png'))
    model.insertRow(0,item )


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        completer = QCompleter()
        self.entry.setCompleter(completer)
        model = QStandardItemModel()
        completer.setModel(model)
        get_data(model)
        self.entry.show()
