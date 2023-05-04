import re
from linebot.models import *

def Wantedimage(message) :
    image_message = ImageSendMessage(
        origional_content_url = 'https://i.imgur.com/I4WfgZI.jpg',
        preview_image_url = 'https://imgur.com/JliRzrH.jpg'
    )
    return image_message