import urllib.parse

import requests
from flask import Flask, request

app = Flask(__name__)

BASE_URL = "https://github.com/login/oauth/"

oauth_info = {
    "client_id": "8d1601b282fc5537222c",
    "client_secret": "51571d07881e59f65b9b6b38e9077b5d154ccc4c",
    "redirect_uri": "http://127.0.0.1:5000/oauth/redirect"
}

# 主页视图
@app.route('/', methods=['GET'])
def index():
    q_string = urllib.parse.urlencode({
        "client_id": oauth_info["client_id"],
        "redirect_uri": oauth_info["redirect_uri"]
    })
    # 组装授权申请地址
    oauth_url = BASE_URL + "/authorize?" + q_string
    return f"<h3><a href='{oauth_url}'>Login</a></h3>"


# 跳转页面视图
@app.route("/oauth/redirect")
def oauth():
    token_url = BASE_URL + "/access_token"
    # 获取授权码
    auth_code = request.args.get("code")
    params = {
        "client_id": oauth_info["client_id"],
        "client_secret": oauth_info["client_secret"],
        "code": auth_code
    }
    headers = {
        "accept": "application/json",
    }
    # 请求令牌
    res = requests.post(token_url, params=params, headers=headers)
    # 获取令牌
    token = res.json().get("access_token")
    # 带上令牌
    headers["Authorization"] = "token " + token
    # 获取用户信息, API 地址为 https://api.github.com/user
    res = requests.get("https://api.github.com/user", headers=headers)

    return f"<h3>{res.json().get('name')}</h3>"


if __name__ == '__main__':
    app.run(debug=True)