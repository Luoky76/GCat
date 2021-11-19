from flask import Flask, request, jsonify
from GEvent import GEvent
import Handler

app = Flask(__name__)

@app.route('/GcatServer', methods=['POST', 'GET'])
def main():
    json_data = dict(request.get_json())
    gEvent = GEvent(json_data)
    gEvent = Handler.EventDistributer(gEvent)
    return jsonify(gEvent.json())


if __name__ == '__main__':
    app.run(debug=True)
