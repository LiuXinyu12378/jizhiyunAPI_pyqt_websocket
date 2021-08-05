from websocket import create_connection
import json
import threading

host = "stage.gizwits.com"
wss_port = "8880"
url_ = "wss://{}:{}/ws/app/v1".format(host, wss_port)
ws = create_connection(url_, timeout=5)

data = {
            "cmd": "login_req",
            "data":
                {
                    "appid": "d0d657adf74c4208b81f0bc5b63ab15b",
                    "uid": "1a9a7f60de914ddf997373ac354fd8b6",
                    "token": "edbc8c2618934a75b7e45debdbe19a2c",
                    "p0_type": "attrs_v4",
                    "heartbeat_interval": 1,
                    "auto_subscribe": "true"
                }
        }

did = {
            "cmd": "subscribe_req",
            "data":
                [
                    {"did": "d2OS9WfUA85rmXjBhhlJAh"}
                ]
        }
write0 = {
            "cmd": "c2s_write",
            "req_sn": 0x0093,  #(可选参数, 若有值下发指令为带ACK的业务透传指令[0x0093], 若无则为不带ACK的业务透传指令[0x0090])
            "data":
            {
            "did": "d2OS9WfUA85rmXjBhhlJAh", #（目标设备的did）
            "attrs":
                {
            "LED": False,  #(“name1”指数据点的标识名(name)， < value1 > 指数据点的值。值可以为true / false(布尔型)，Unicode编码的字符串如\u62bd(枚举型)，数字（数值型），byte数组[23, 2, 3]（扩展类型)
                }}}
write1 = {
            "cmd": "c2s_write",
            "req_sn": 0x0093,  #(可选参数, 若有值下发指令为带ACK的业务透传指令[0x0093], 若无则为不带ACK的业务透传指令[0x0090])
            "data":
            {
            "did": "d2OS9WfUA85rmXjBhhlJAh", #（目标设备的did）
            "attrs":
                {
            "LED": True,  #(“name1”指数据点的标识名(name)， < value1 > 指数据点的值。值可以为true / false(布尔型)，Unicode编码的字符串如\u62bd(枚举型)，数字（数值型），byte数组[23, 2, 3]（扩展类型)
                }}}
read = {
    "cmd": "c2s_read",
    "req_sn": 0x0093,  # (可选参数, 若有值下发指令为带ACK的业务透传指令[0x0093], 若无则为不带ACK的业务透传指令[0x0090])
    "data":
        {
            "did": "d2OS9WfUA85rmXjBhhlJAh",  # （目标设备的did）
            "names": ["LED"]  # （变长数据点可选参数：传入需要读取的数据点名称，参数省略表示读取全部数据点；定长数据点读操作忽略该参数）
        }
}
ping = {
    "cmd": "ping"
}

data = json.dumps(data)
did = json.dumps(did)
write1 = json.dumps(write1)
write0 = json.dumps(write0)
read = json.dumps(read)
ping = json.dumps(ping)


def send_led1():
    sub_thread = threading.Thread(target=ws.send,args=[write0])
    sub_thread.start()



def send_led0():
    sub_thread = threading.Thread(target=ws.send,args=[write1])
    sub_thread.start()

