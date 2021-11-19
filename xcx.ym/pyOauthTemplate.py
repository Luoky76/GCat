#A cool template for implementing OAuth2 in python.
#It is bringing best of both requests_oauthlib and requests for creating apps using OAuth2
#When you create any app in any website you are given client_id,client_secret and should register a redirect URI
#Any API website provides OAuth_url,Token_url in their docs.That's it, just replace every < > thing and run program 
#You collect access token in variable token,store it in a DB to process later


from flask import Flask, redirect, request, session
from requests_oauthlib import OAuth2Session
import requests
from requests.auth import HTTPBasicAuth


app = Flask(__name__)

client_id = '<your_client_id'
client_secret = '<your_client_secret'
redirect_uri = 'http://127.0.0.1:5000/support'
autherize ='<OAuth_url of website>'
grant_type='authorization_code'
token_uri='<Token_url of website>'
token=None



@app.route("/")
def hello():
    push = OAuth2Session(client_id, redirect_uri=redirect_uri)
    authorization_url, states = push.authorization_url(autherize)
    return redirect(authorization_url)


@app.route("/support", methods=['GET'])
def support():
    global token
    code = str(request.args['code'])
    print(code)
    getpayload = {'client_id':client_id, 'client_secret':client_secret, 'grant_type': grant_type, 'code': code}
    res = requests.post(token_uri, data=getpayload)
    h = res.json()
    token = h['access_token']
    return redirect('/hai')


@app.route("/hai")
def hai():
    global token
    return 'Token is %s' % (token)
    
    
if __name__ == "__main__":
    app.run(threaded=True)
