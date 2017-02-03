from PyQt5.QtWidgets import *


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        self.list = QListWidget(root)
        self.list.IconMode
        self.entry.move(700, 200)
        self.list.move(700,225)
        self.list.IconMode
        self.trigger()

    def trigger(self):
        self.entry.textChanged[str].connect(self.code_ac)

    def code_ac(self, text):
        if len(self.list) != 0:
            self.list.clear()
        ref = open("../../Lib/reference.lib", "r")
        for line in ref:
            if text == line[:len(text)]:
                self.list.addItem(line)
