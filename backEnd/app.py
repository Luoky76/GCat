from flask import Flask, request, json
from GEvent import GEvent
from exts import db
from models import Record
import config
import Handler

app = Flask(__name__)


@app.route('/GcatServer', methods=['POST'])
def main():
    json_data = dict(request.get_json())
    gEvent = GEvent(json_data)
    gEvent = Handler.EventDistributer(gEvent)
    return gEvent


if __name__ == '__main__':
    app.run(debug=True)
