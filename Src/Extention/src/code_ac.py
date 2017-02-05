from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import QSize


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        self.list = QListWidget(root)
        self.list.setIconSize(QSize(12, 12))
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
            print(text)
            for line in ref:
                if text == line[:len(text)]:
                    #lstitem.setIcon(QIcon("../Img/event.png"))
                    self.list.addItem(line[:-1])
                    index += 1
            if index < 5:
                self.list.setFixedHeight(font_size * index)
            else:
                self.list.setFixedHeight(120)
            ref.close()
