from flask import Flask,request,json
from GEvent import GEvent
app = Flask(__name__)

@app.route('/GcatServer',methods=['POST'])
def main():
    json_data=request.get_json()
    eventRequest=GEvent(json_data)
    #msg="recive an GEvent! ID:{}".format(eventRequest.eventID)

    return "Recive a GEvent"

if __name__ == '__main__':
    app.run(debug=True)
