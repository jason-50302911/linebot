import re 
from linebot.models import *

def Wantedvideo(message):
    if re.match('影片', message):
        video_message = VideoSendMessage(
            original_content_url= 'https://imgur.com/G7MgBG0.mp4',
            preview_image_url = 'https://imgur.com/JliRzrH.jpg',
            durtion = 1500
        )
  