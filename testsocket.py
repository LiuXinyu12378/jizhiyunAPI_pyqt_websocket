import threading
import time
import json
import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon
from utils import data, did, read, ping, ws, btnstate, btnstate2

app = QApplication(sys.argv)
# print(QIcon('icon.png'))
app.setWindowIcon(QIcon('icon.png'))
QMainWindow = QMainWindow()
ui = untitled.Ui_dialog()
ui.setupUi(QMainWindow)
QMainWindow.show()

ui.radioButton.toggled.connect(lambda: btnstate(ui.radioButton))
ui.radioButton_2.toggled.connect(lambda: btnstate(ui.radioButton_2))
ui.radioButton_3.toggled.connect(lambda: btnstate2(ui.radioButton_3))
ui.radioButton_4.toggled.connect(lambda: btnstate2(ui.radioButton_4))



def read_data():
    while True:
        try:
            ws.send(read)
            recv = json.loads(ws.recv())
            if recv.get('data'):
                attrs = recv.get('data').get('attrs')
                data = {
                    "灯1": attrs.get('LED'),
                    "灯2": attrs.get('LED2'),
                    "温度": attrs.get('wendu'),
                    "湿度": attrs.get('shidu'),
                    "人体感应": attrs.get('rentiganying'),
                    "土壤湿度": attrs.get('turangshidu'),
                    "空调": attrs.get('pwm1'),
                    "风扇": attrs.get('pwm2'),
                }
                ui.label_6.setText(str(round(data['温度'],2))+" ℃")
                ui.label_7.setText(str(round(data['湿度'],2))+ " %")
                ui.label_11.setText(str(round(data['土壤湿度'],2))+ " %")

                if data["人体感应"] == True:
                    ui.label_9.setText("Somebody In!!!")
                else:
                    ui.label_9.setText("Nobody")
                ui.textEdit.append(str(data))
                time.sleep(0.5)
        except EnvironmentError as e:
            ui.textEdit.append("远程客户端网络断开！等待连接。。。")
            print(e)

def heart():
    while True:
        try:
            ws.send(ping)
            recv = ws.recv()
            time.sleep(5)
        except EnvironmentError as e:
            print(e)

def init_ihome():
    try:
        ws.send(data)
        ui.textEdit.append(ws.recv())
        ws.send(did)
        ui.textEdit.append(ws.recv())
    except EnvironmentError as e:
        print(e)

if __name__ == '__main__':
    if ws.connected:
        init_ihome()
        sub_thread_heart = threading.Thread(target=heart)
        sub_thread_read = threading.Thread(target=read_data)

        sub_thread_heart.start()
        sub_thread_read.start()
        sys.exit(app.exec_())
