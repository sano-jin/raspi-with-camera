# from picamera import PiCamera
from time import sleep, time
import requests
import json
import os
from dotenv import load_dotenv

slack_api = 'https://slack.com/api'
ID_PATH = '/home/pi/id.log'
IMG_PATH = '/home/pi/image.jpg'
TOKEN = ''
CHANNEL = ''
APPID = 'A019NGRQWET'

def load_env():
    global TOKEN, CHANNEL
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    CHANNEL = os.getenv('CHANNEL')

def take_pic():
    camera = PiCamera()
    camera.start_preview()
    sleep(3)
    camera.capture(IMG_PATH)
    camera.stop_preview()

def upload():
    files = {'file': open(IMG_PATH, 'rb')}
    param = {'token': TOKEN, 'channels': CHANNEL,
             'filename': 'filename', 'title': 'title'}
    requests.post(
        slack_api+"/files.upload", params=param, files=files)
    
def delete():
    diff = 60 * 60 # 1 hour
    param = {'token': TOKEN, 'ts_to': time.time() - diff, 'user' : APPID}
    res = requests.post(
        slack_api+"/files.list", params=param)
    
    def post_delete( file_json ):
        param = {'token': TOKEN, 'file': file_json['id']}
        requests.post(
            slack_api+"/files.delete", params=param)

    map( lambda file_json: post_delete(file_json), res.json()['files'] )

if __name__ == '__main__':
    load_env()
    # print(TOKEN, CHANNEL)

    # take_pic()
    # upload()
    # delete()
