from PyQt5.QtWidgets import *


class CodeAC:

    def __init__(self, root):
        self.entry = QLineEdit(root)
        self.list = QListView(root)
        self.entry.move(700, 200)
        self.list.move(700,225)
        self.list.setViewMode(QListView.IconMode)
        self.trigger()

    def trigger(self):
        self.entry.textChanged[str].connect(self.code_ac)

    def code_ac(self, text):
        ref = open("reference.lib", "r")
        for line in ref:
            if text == line[1]:
