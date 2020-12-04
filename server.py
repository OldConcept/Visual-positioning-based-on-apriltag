'''
Author: OldConcept
Date: 2020-12-04 07:37:29
LastEditors: OldConcept
LastEditTime: 2020-12-05 03:11:24
FilePath: \py\rm_server\server.py
'''
from flask import Flask, request, jsonify
import comm
import t1
# import shoot
import threading

# 后端程序启动
app = Flask(__name__)

success_message = {
    "success": 1
}

value = [0, 0, 0, 0]
shoot_order = [0, 0, 0]

@app.route('/test', methods=['GET'])
def test():
    if request.method == "GET":
        return jsonify(success_message)

@app.route('/setSpeed', methods=['GET'])
def setSpeed():
    if request.method == "GET":
        motor_1 = request.args.get("motor1")
        motor_2 = request.args.get("motor2")
        motor_3 = request.args.get("motor3")
        motor_4 = request.args.get("motor4")
        value[0] = int(motor_1)
        value[1] = int(motor_2)
        value[2] = int(motor_3)
        value[3] = int(motor_4)
        # 调用串口发送函数给下位机发送速度数据
        comm.transferParam(0, value)
        return jsonify(success_message)

@app.route('/fire', methods=['GET'])
def fire():
    if request.method == "GET":
        first_tag = request.args.get("tag1")
        second_tag = request.args.get("tag2")
        third_tag = request.args.get("tag3")
        shoot_order[0] = first_tag
        shoot_order[1] = second_tag
        shoot_order[2] = third_tag
        # TODO
        # 调用射击函数
        t = threading.Thread(target=t1.detect, args=())
        t.start()
        return jsonify(success_message)

@app.route('/ceasefire', methods=['GET'])
def ceasefire():
    if request.method == "GET":
        # TODO
        # 设置全局标志，放在while处理每一帧图像之前处理，标志位为真再进行图像处理
        return jsonify(success_message)

@app.route('/checkTagNum', methods=['GET'])
def checkTagNum():
    if request.method == "GET":
        # TODO
        # 调用api返回当前时刻摄像头中的tag数量
        tagNum = 233
        return jsonify({
            "tagNum": tagNum
        })

@app.route('/setServo', methods=['GET'])
def setServo():
    if request.method == "GET":
        mode = request.args.get("mode")
        print(f'mode->{mode}')
        # TODO
        # 调整舵机
        return jsonify(success_message)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9600)
    print("server down")