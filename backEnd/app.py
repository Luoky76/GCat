from flask import Flask, request, json
from GEvent import GEvent
import handler

app = Flask(__name__)


@app.route('/GcatServer', methods=['POST'])
def main():
    json_data = dict(request.get_json())
    gEvent = GEvent(json_data)
    print(11111111111111)
    gEvent = handler.EventDistributer(gEvent)
    
    return gEvent


if __name__ == '__main__':
    app.run(debug=True)
