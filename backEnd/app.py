from flask import Flask, request, jsonify
from gevent import GEvent
from handlers import EventDistributer

app = Flask(__name__)


@app.route('/GcatServer', methods=['POST', 'GET'])
def main():
    gEvent = GEvent(dict(request.get_json()))  # 提取报文GEvent信息
    gEvent = EventDistributer(gEvent)  # 分发获取需求内容
    return jsonify(gEvent.toJson())  # 返回json报文


if __name__ == '__main__':
    # 多线程启动后端服务器
    app.run(debug=True, threaded=True)
