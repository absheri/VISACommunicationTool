from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        self.list = QListWidget(root)
        self.entry.move(400, 200)
        self.list.move(400,225)
        self.trigger()

    def trigger(self):
        self.entry.textChanged[str].connect(self.code_ac)

    def code_ac(self, text):
        self.list.clear()
        index = 0
        font_size = 22
        # row line height
        ref = open("../../Lib/reference.lib", 'r')
        if text:
            for line in ref:
                if text == line[:len(text)]:
                    lstitem = QListWidgetItem(line[:-1])
                    lstitem.setIcon(QIcon("..\..\Src\Img\O.png"))
                    self.list.insertItem(index, lstitem)
                    index += 1
            ref.close()
        if index < 5:
            self.list.setFixedHeight(font_size * index)
        else:
            self.list.setFixedHeight(120)
