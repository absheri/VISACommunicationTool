# VISA Communication Tool
This project aims to take advantages of PyVisa to create a light-weight T&M (Test & Measurement) instrument communicate software.

## Three Parts
   -  [GUI.py](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Main/GUI.py) - Graphic User Interface
    -  [code_ac.py](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Extention/src/code_ac.py) - Code Auto Complete & Query Tool
    -  [communication.py](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Extention/src/communication.py) - VISA Communication Interface

## How to Run thes Demo

Since we have not encapsulated the project, you can directly run GUI.py to check the software. However, three external python packagess are necessary: **PyQt5**, **PyVISA**, and **Pandas**.  To demo all functionality, a Tektronix Instrument and NI VISA are necessary. If instrument or NI VISA is not detected, the software will use some hard coded parameters and disable the communication interface.

Run our project with PyCharm (**Recommanded**)
 - Download and Install [PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
 - Import Our Project
 - Set up project interpreter with necessary packages: **PyQt5**, **PyVISA**, and **Pandas** with help of this [file](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/SetUp)
 - Run GUI.py

All packages can be installed via pip from PyPI
```
>> pip install pandas
>> pip3 install install pyqt5
>> pip install -U pyvisa
```

Run our project from terminal.

```
>> python GUI.py
```
## Quick View















