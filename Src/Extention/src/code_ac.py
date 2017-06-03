import pandas as pd
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
            cmd.update({str(item): 1})
    return cmd


def query_csv_dpo():
    data = pd.read_csv("..\..\Src\Lib\DPO.csv", encoding="ISO-8859-1", header=None,
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
            cmd.update({str(item): 1})
    return cmd


def model_content(connect_model):
    if 'AWG' in connect_model:
        result = query_csv_awg()
    elif 'DPO'in connect_model:
        result = query_csv_dpo()
    else:
        result = None
    return result


def get_data(model, device):
    result = model_content(device)
    icon_address = ['..\..\Src\Img\A.png', '..\..\Src\Img\O.png']
    index = 0;
    if result is not None:
        for cmd, value in result.items():
            item = QStandardItem(cmd)
            item.setIcon(QIcon(icon_address[value]))
            model.insertRow(index, item)
            index += 1
    else:
        item = QStandardItem(" ")
        item.setIcon(QIcon(icon_address[1]))
        model.insertRow


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
        super(DocQuery,self).__init__(parent)
        self.setFixedSize(800,800)
        self.device = device
        self.keyword_in = QLineEdit(self)
        self.search_button = QPushButton("Go", self)
        self.select_group = QComboBox(self)
        self.select_group.addItems(['All','Acquisition', 'Act on Event', 'AFG', 'Alias','ARB', 'Bus','Calibration and Diagnostic','Configuration', 'Cursor', 'Display','DVM', 'Email', 'Ethernet', 'File System', 'Hard Copy', 'Histogram','Horizontal''Mark', 'Mask', 'Math', 'Measurement', 'Miscellaneous', 'PictBridge', 'Power','RF', 'Save and Recall', 'Search', 'Status and Error', 'Trigger', 'Vertical','Video Picture', 'Waveform Transfer', 'Zoom'])
        self.query_option = QCheckBox('Query Only',self)
        self.search_button.clicked.connect(self.doc_search)
        self.doc_display = QScrollArea(self)
        self.doc_display.setStyleSheet("background-color: lightgray")
        self.grid_layout = QGridLayout(self)
        self.grid_layout.setSpacing(20)
        self.grid_layout.addWidget(self.keyword_in, 2, 0)
        self.grid_layout.addWidget(self.search_button, 2, 1)
        self.grid_layout.addWidget(self.select_group, 1, 0)
        self.grid_layout.addWidget(self.query_option, 1, 1)
        self.grid_layout.addWidget(self.doc_display, 3, 0, 5, 0)
        self.setWindowTitle("Search Documentation")
        if 'AWG' in self.device:
            self.data = pd.read_csv("..\..\Src\Lib\AWG.csv", encoding="ISO-8859-1", header=None)
        elif 'DPO' in self.device:
            self.data = pd.read_csv("..\..\Src\Lib\DPO.csv", encoding="ISO-8859-1", header=None)
        else:
            self.data = pd.read_csv("..\..\Src\Lib\DPO.csv", encoding="ISO-8859-1", header=None)

    def doc_search(self):
        key = self.keyword_in.text()
        group = str(self.select_group.currentText())
        query_only = self.query_option.isChecked()
        q_mark = None
        if query_only is True:
            q_mark = '?'
        # print format

        if group == 'All' and query_only:
            query_info = self.data[(self.data[7].str.contains(key) == True) & (self.data[2].notnull())]
        elif group == 'All' and query_only == False:
            query_info = self.data[(self.data[7].str.contains(key) == True)]
        elif group != 'All' and query_only:
            query_info = self.data[(self.data[7].str.contains(key) == True) & (self.data[2].notnull()) & (self.data[0].str.contains(group) == True)]
        else:
            query_info = self.data[(self.data[7].str.contains(key) == True) & (self.data[0].str.contains(group) == True)]
        Group = []
        Syntax = []
        Query = []
        Return = []
        Argument = []
        Example = []
        Description = []
        for element in query_info[0]:
            Group.append(str(element))
        for element in query_info[1]:
            Syntax.append(str(element))
        for element in query_info[2]:
            Query.append(str(element))
        for element in query_info[3]:
            Return.append(str(element))
        for element in query_info[5]:
            Argument.append(str(element))
        for element in query_info[6]:
            Example.append(str(element))
        for element in query_info[7]:
            Description.append(str(element))
        ####
        W = QWidget(self)
        w_layout = QGridLayout(self)
        for index in range(len(query_info[0])):
            s_display = QLabel(self)
            s_display.setText(Syntax[index])
            s_display.setStyleSheet('color: blue')
            g_display = QLabel(self)
            g_display.setText(Group[index])
            q_display = QLabel(self)
            q_display.setText(Query[index])
            r_display = QLabel(self)
            r_display.setText(Return[index])
            a_display = QLabel(self)
            a_display.setText(Argument[index])
            e_display = QLabel(self)
            e_display.setText(Example[index])
            d_display = QLabel(self)
            d_display.setText(Description[index])

            label = QLabel(self)
            label.setText("SYNTAX")
            label.setStyleSheet('color: darkblue')
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 1 + index * 7, 0)
            w_layout.addWidget(s_display, 1 + index * 7, 1)

            label = QLabel(self)
            label.setText("      Group")
            label.setFont(QFont("Times",weight=QFont.Bold))
            w_layout.addWidget(label, 2+index*7,0)
            w_layout.addWidget(g_display, 2+index*7,1)

            label = QLabel(self)
            label.setText("      Query")
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 3+index*7, 0)
            w_layout.addWidget(q_display, 3+index*7, 1)
            label = QLabel(self)
            label.setText("      Return")
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 4+index*7, 0)
            w_layout.addWidget(r_display, 4+index*7, 1)
            label = QLabel(self)
            label.setText("      Argument")
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 5+index*7, 0)
            w_layout.addWidget(a_display, 5+index*7, 1)
            label = QLabel(self)
            label.setText("      Example")
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 6+index*7, 0)
            w_layout.addWidget(e_display, 6+index*7, 1)
            label = QLabel(self)
            label.setText("      Description")
            label.setFont(QFont("Times", weight=QFont.Bold))
            w_layout.addWidget(label, 7+index*7, 0)
            w_layout.addWidget(d_display,  7+index*7, 1)
        W.setLayout(w_layout)
        self.doc_display.setWidget(W)