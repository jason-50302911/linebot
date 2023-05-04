import re
from linebot.models import *

def WantedButtons(message):
    buttons_template_message = TemplateSendMessage(
                alt_text = '這個是按鈕',
                template = ButtonsTemplate(
                    thumbnail_image_url = 'https://i.imgur.com/I4WfgZI.jpg',
                    text = '選單功能- TemplateSendMessage',
                    actions = [
                        PostbackAction (
                            label = '偷偷的傳訊息',
                            display_text = '檯面上',
                            data = '檯面下'
                        ),
                        MessageAction(
                            label = '直接傳訊息',
                            text = '資料'
                        ),
                        URIAction(
                            label = '稍等一下',
                            uri = 'https://i.imgur.com/I4WfgZI.jpg'
                        )
                    ]
                )
            )