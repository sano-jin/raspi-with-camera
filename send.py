import requests
import json

TOKEN = # 取得したトークン
CHANNEL = # チャンネルID

files = {'file': open("figure.png", 'rb')}
param = {
    'token':TOKEN, 
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}

requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
