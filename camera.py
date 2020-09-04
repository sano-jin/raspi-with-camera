import requests
import json
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()

sleep(3)

camera.capture('/home/pi/image.jpg')

camera.stop_preview()

files = {'file': open("/home/pi/image.jpg", 'rb')}
param = {
    'token':TOKEN, 
    'channels':CHANNEL,
    'filename':"filename",
    'initial_comment': "initial_comment",
    'title': "title"
}

requests.post(url="https://slack.com/api/files.upload",params=param, files=files)
