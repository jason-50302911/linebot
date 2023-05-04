from linebot.models import *
import re 

def Wantedsticker(message):
    if re.match('我好餓', message):
        sticker_message = StickerSendMessage(
          package_id = '446',
          sticker_id = '1990'
        )   
    elif re.match('你好', message):
        sticker_message = StickerSendMessage(
            package_id = '446',
            sticker_id = '1993'
        )
    return sticker_message

    