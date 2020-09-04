# from picamera import PiCamera
from time import sleep
import requests
import json
import os
from dotenv import load_dotenv

slack_api = 'https://slack.com/api'
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
    camera.capture('/home/pi/image.jpg')
    camera.stop_preview()

# upload file and return id
def upload():
    files = {'file': open('/home/pi/image.jpg', 'rb')}
    param = {'token': TOKEN, 'channels': CHANNEL,
             'filename': 'filename', 'title': 'title'}
    res = requests.post(
        slack_api+"/files.upload", params=param, files=files)
    return res.json()['file']['id']
    
def delete(id):
    param = {'token': TOKEN, 'file': id}
    r_post = requests.post(
        slack_api+"/files.delete", params=param)



if __name__ == '__main__':
    load_env()
    # print(TOKEN, CHANNEL)

    # take_pic()
    # upload()
