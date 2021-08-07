import threading
import time
import json
import sys
import untitled
from PyQt5.QtWidgets import QApplication,QMainWindow
from utils import data,did,read,ping,ws

app = QApplication(sys.argv)
QMainWindow = QMainWindow()
ui = untitled.Ui_dialog()
ui.setupUi(QMainWindow)
QMainWindow.show()


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
                ui.label_6.setText(str(data['温度']))
                ui.label_7.setText(str(data['湿度']))
                ui.textEdit.append(str(data))
                time.sleep(0.5)
        except EnvironmentError as e:
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
