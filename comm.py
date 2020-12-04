'''
Author: OldConcept
Date: 2020-12-04 09:26:20
LastEditors: OldConcept
LastEditTime: 2020-12-05 02:34:01
FilePath: \py\rm_server\comm.py
'''
import serial
import serial.tools.list_ports
import time
import threading

portx = "/dev/ttyACM1"
bps = 115200
timex = None
ser = serial.Serial(portx, bps, timeout = timex)

# type = {0, 1}
# value = [0, 0, 0, 0]
# 0表示给下位机传递电机速度控制小车，传入的值为一个数组

def sendData(str):
    ser.write(str.encode())

def transferParam(type, value):
    threads = []
    if type == 0:
        if value[0] > 0:
            t1 = threading.Thread(target=sendData, args=('M01,'+'{:0>3d}'.format(value[0])+';',))
        else:
            value[0] = abs(value[0])
            t1 = threading.Thread(target=sendData, args=('M05,'+'{:0>3d}'.format(value[0])+';',))
        if value[1] > 0:
            t2 = threading.Thread(target=sendData, args=('M02,'+'{:0>3d}'.format(value[1])+';',))
        else:
            value[1] = abs(value[1])
            t2 = threading.Thread(target=sendData, args=('M06,'+'{:0>3d}'.format(value[1])+';',))
        if value[2] > 0:
            t3 = threading.Thread(target=sendData, args=('M03,'+'{:0>3d}'.format(value[2])+';',))
        else:
            value[2] = abs(value[2])
            t3 = threading.Thread(target=sendData, args=('M07,'+'{:0>3d}'.format(value[2])+';',))
        if value[3] > 0:
            t4 = threading.Thread(target=sendData, args=('M04,'+'{:0>3d}'.format(value[3])+';',))
        else:
            value[3] = abs(value[3])
            t4 = threading.Thread(target=sendData, args=('M08,'+'{:0>3d}'.format(value[3])+';',))
        threads.append(t1)
        threads.append(t2)
        threads.append(t3)
        threads.append(t4)
    if type == 1:
        t1 = threading.Thread(target=sendData, args=('M09,'+'{:0>3d}'.format(value[0])+';',))
        t2 = threading.Thread(target=sendData, args=('M10,'+'{:0>3d}'.format(value[1])+';',))
        threads.append(t1)
        threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
        t.join()

def test(value):
    for v in value:
        print(v)
