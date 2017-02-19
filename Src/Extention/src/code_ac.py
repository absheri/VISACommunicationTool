from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


def get_data(model):
    # Searching through the Doc
    # Result shows in a dictionary structure
    result = {"alpha": 0, "apple": 1, "agree": 2}
    icon_address = ['..\..\Src\Img\A.png', '..\..\Src\Img\E.png','..\..\Src\Img\O.png']
    for cmd, value in result.items():
        item = QStandardItem(cmd)
        item.setIcon(QIcon(icon_address[value]))
        model.insertRow(0, item)


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        completer = QCompleter()
        self.entry.setCompleter(completer)
        model = QStandardItemModel()
        completer.setModel(model)
        get_data(model)
        self.entry.show()
