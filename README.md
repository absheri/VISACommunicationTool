# VISA Communication Tool
    This project aims to take advantages of PyVisa to create a light-weight T&M (Test & Measurement) instrumentS
    communicate software.

## This project mainly contains three parts
    - Graphic User Interface [GUI.py](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Main/GUI.py)
    - Code Auto Complete & Query Tool [code_ac.py](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Extention/src/code_ac.py)
    - VISA Communication [communication](https://github.com/HouPoc/VISACommunicationTool-GROUP64/blob/master/Src/Extention/src/communication.py)

## How to run this demo
    Since we have not encapsulated the project, you can directly run [GUI.py] to use the software. To demo all functionality, a Tektronix Instrument is
    necessary. If no instrument is detected, the software will use some hard coded parameter and disable the communication interface.

