from picamera import PiCamera
from time import sleep
import requests
import json
TOKEN =	#                                                                               
CHANNEL = #                                                                             

camera = PiCamera()
camera.start_preview()
sleep(3)
camera.capture('/home/pi/image.jpg')
camera.stop_preview()

files = {'file' : open('/home/pi/image.jpg', 'rb')}
param = {'token' : TOKEN, 'channels': CHANNEL}
r_post = requests.post("https://slack.com/api/files.upload", params = param, files = files)
# print( r_post.json() ) 
