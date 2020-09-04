# from picamera import PiCamera
from time import sleep
import requests
import json
import os
from dotenv import load_dotenv

slack_api = 'https://slack.com/api'
ID_PATH = '/home/pi/id.log'
IMG_PATH = '/home/pi/image.jpg'
TOKEN = ''
CHANNEL = ''


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

# upload file and write id to ID_PATH
def upload():
    files = {'file': open(IMG_PATH, 'rb')}
    param = {'token': TOKEN, 'channels': CHANNEL,
             'filename': 'filename', 'title': 'title'}
    res = requests.post(
        slack_api+"/files.upload", params=param, files=files)
    file_id = res.json()['file']['id']
    f = open(ID_PATH, 'w')
    f.write(file_id)
    f.close
    
# read id from ID_PATH and delete
def delete():
    f = open(ID_PATH, 'r')
    file_id = f.read()
    f.close()
    param = {'token': TOKEN, 'file': file_id}
    requests.post(
        slack_api+"/files.delete", params=param)


if __name__ == '__main__':
    load_env()
    # print(TOKEN, CHANNEL)

    # take_pic()
    # upload()
