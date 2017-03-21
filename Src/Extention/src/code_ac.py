from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import csv


def query_csv_awg():
    reader = csv.reader(open("..\..\Src\Lib\AWG.csv", "rt"))
    cmd = {}
    for row in reader:
        if row[1] is not None:
            if '?' not in row[1]:
                cmd.update({row[1]: 0})
            else:
                cmd.update({row[1]: 1})
        if row[2] is not None:
            cmd.update({row[2]:1})
    return cmd


def query_csv_afg():
    return 1


def query_csv_mdo():
    return 1


def query_csv_mdd():
    return 1


def model_content(connect_model):
    if 'AWG' in connect_model:
        result = query_csv_awg()
    #elif 'AFG'in connect_model:
    #    result = query_csv_afg()
    #elif 'MDO'in connect_model:
    #    result = query_csv_mdo()
    #elif 'MSO' in connect_model or 'DPO' in connect_model or 'DSA' in connect_model:
    #    result = query_csv_mdd()
    else:
        result = None
    return result


def get_data(model, device):
    # Searching through the Doc
    # Result shows in a dictionary structure
    result = model_content(device)
    icon_address = ['..\..\Src\Img\A.png', '..\..\Src\Img\E.png']
    index = 0;
    for cmd, value in result.items():
        item = QStandardItem(cmd)
        item.setIcon(QIcon(icon_address[value]))
        model.insertRow(index, item)
        index += 1


class CodeAC:
    def __init__(self, input_line, device):
        self.completer = QCompleter()
        input_line.setCompleter(self.completer)
        self.model = QStandardItemModel()
        self.input_line = input_line
        self.device = device

    def active_script(self):
        get_data(self.model, self.device)
        self.completer.setModel(self.model)
        self.completer.activated.connect(self.tip_balloon)

    def tip_balloon(self, text):
        # selected highlight item
        self.input_line.setToolTip("none")


