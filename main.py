# from picamera import PiCamera
from time import sleep, time
import requests
import json
import os
from dotenv import load_dotenv

slack_api = 'https://slack.com/api'
IMG_PATH = 'image.jpg'
TOKEN = ''
CHANNEL = ''
USERID = ''

def load_env():
    global TOKEN, CHANNEL, USERID
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    CHANNEL = os.getenv('CHANNEL')
    USERID = os.getenv('USERID')

def take_pic():
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture(IMG_PATH)
    camera.stop_preview()

def upload():
    files = {'file': open(IMG_PATH, 'rb')}
    param = {'token': TOKEN, 'channels': CHANNEL,
             'filename': 'test-file', 'title': 'this is a test'}
    requests.post(
        slack_api+"/files.upload", params = param, files = files)

def delete():
    diff = 60 * 30 # 30 minutes
    param = {'token': TOKEN, 'ts_to': time() - diff, 'types' : 'images'}
    res = requests.post(
        slack_api+"/files.list", params = param)
    # print(json.dumps(res.json(), indent = 1))

    for file_json in res.json()['files']:
        if file_json['user'] != USERID:
            continue
        param = {'token': TOKEN, 'file': file_json['id']}
        dlt_res = requests.post(
            slack_api+"/files.delete", params = param)
        # print(json.dumps(dlt_res.json(), indent = 1))

if __name__ == '__main__':
    load_env()
    # print(TOKEN, CHANNEL, USERID)

    # take_pic()
    # upload()
    # delete()
