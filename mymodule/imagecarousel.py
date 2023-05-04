import re
from linebot.models import *

def Wantedimagecarousel(message):
    image_carousel_message = TemplateSendMessage(
        alt_text = '我看不到',
        template = ImageCarouselTemplate(
            columns = [
                ImageCarouselColumn(
                    image_url = 'https://i.imgur.com/I4WfgZI.jpg',
                    action = PostbackAction(
                        label = '我教你武功',
                        display_text = '很厲害嘛',
                        data = 'Are You Sure'
                    )
                ),
                ImageCarouselColumn(
                    image_url = 'https://imgur.com/o8F1E49.jpg',
                    action = MessageAction(
                        label = '我操',
                        text = '優'
                    )
                )
            ]
        )
    )