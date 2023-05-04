from linebot.models import *
import re 

def WantedSendloction(message):
    if re.match('我的學校', message):
      location_message = LocationSendMessage(
          title = '高雄的學校',
          address = '我的學校',
          latitude = 22.78757415480277,
          longitude = 120.40710230230081
      ) 
    elif re.match('高雄科技大學', message):
      location_message = LocationSendMessage(
          title = '高雄的學校',
          address = '高科',
          latitude = 22.772401996463415,
          longitude = 120.40013954026035
      ) 
    return location_message
