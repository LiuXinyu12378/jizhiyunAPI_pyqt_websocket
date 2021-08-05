import threading
import time
import json
import sys
import design
from PyQt5.QtWidgets import QApplication,QMainWindow
from utils import data,did,write0,write1,read,ping,ws

app = QApplication(sys.argv)
QMainWindow = QMainWindow()
ui = design.Ui_Dialog()
ui.setupUi(QMainWindow)
QMainWindow.show()




def heart():
    while True:
        try:
            ws.send(ping)
            recv = ws.recv()   #json.loads(ws.recv())
            # print(recv)
            # ui.textEdit.append(recv)
            ws.send(read)
            recv = json.loads(ws.recv())
            if recv.get('data'):
                attrs = str(recv.get('data'))
                ui.textEdit.append(attrs)
            time.sleep(1)
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
        sub_thread = threading.Thread(target=heart)
        sub_thread.start()
        sys.exit(app.exec_())
