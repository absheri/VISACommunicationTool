from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import pandas as pd


def query_csv_awg():
    data = pd.read_csv("..\..\Src\Lib\AWG.csv",  encoding="ISO-8859-1", header=None,
                       usecols=[1, 2])
    cmd = {}
    for item in data[1]:
        if str(item) is not None:
            if '?' not in str(item):
                cmd.update({str(item): 0})
            else:
                cmd.update({str(item): 1})
    for item in data[2]:
        if str(item) is not None:
            cmd.update({str(item):1})
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


class DocQuery(QDialog):

    def __init__(self, parent=None, device=None):
        super().__init__(parent)
        self.device = device
        label_keyword = QLabel("Keyword",self)
        keyword_in = QLineEdit(self)
        search_button = QPushButton("Go", self)
        #search_button.clicked.connect(self.doc_search)
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(10)
        self.grid_layout.addWidget(label_keyword, 1, 0)
        self.grid_layout.addWidget(keyword_in, 1, 1)
        self.grid_layout.addWidget(search_button, 2, 0)

   # def doc_search(self):
   #     key = self.keyword_in.text()
   #     group = self.group_in.text()
   #     reader = csv.reader(open("..\..\Src\Lib\AWG.csv", "rt"))
   #     for row in reader:

