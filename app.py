#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

import time
import re
from mongo_db_function import *
from smallgame import *

# 我個人自己所建立函式
import mymodule.sticker as sticker
import mymodule.location as Loc

app = Flask(__name__)

yourID = 'U74815e99a6860985d7553bab6ada456f'
yourtoken = 'aILAZhOf/dDPjadxBoso186UHS8VhR+Xym3tBoISWKjx4lhd1hIDC+hDBhAA8CqKBKMpS6n1NPKoXfjDjSp2CKSxTDC7N/iaTdGxKRuXW2tDfGd1pbOhHuGsjW2fJjR0oOU3ymRkijwKUwiKE+S0LgdB04t89/1O/w1cDnyilFU='
yourhook = '0cb6ef9eb703460a47e6e38907e61108'

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(yourtoken)
# 必須放上自己的Channel Secret
handler = WebhookHandler(yourhook)

line_bot_api.push_message(yourID, TextSendMessage(text='更新完成'))


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    
  
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



#訊息傳遞區塊
##### 基本上程式編輯都在這個function ##### 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text
    user_id = event.source.user_id
    if check_profile_exist(user_id) is False:
        content = {"User_id": user_id, "status": "Nothing"}
        store_profile(content)
        
    if re.match('玩遊戲', message):
        flex_message = TextSendMessage(
            text = '此遊戲為猜數字，會告訴你幾A幾B，A為位置對數字對，B為位置不對但數字對(最多可以猜五位數)',
            quick_reply = QuickReply(
                items = [
                    QuickReplyButton(action = MessageAction(label = '玩', text = '玩')),
                    QuickReplyButton(action = MessageAction(label = '不玩', text = '不玩'))
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
        
    elif re.match('玩', message):
        status = "initialize_a"
        update_status(user_id,status)
        message_auto = "輸入想猜幾位數數字(一到五位數)"
        if check_game_exist(user_id) is False:
            store_game(user_id)
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message_auto))
    
    elif find_profile(user_id)["status"] == "initialize_a":
        if decsidethedigits(message) == True:
            computeranswer = generatoranswer(message)
            status = "start_play"
            update_status(user_id, status)
            update_game(user_id, computeranswer)
            message_auto = "輸入你猜測的答案"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message_auto))
        else:
            message_auto = "輸入正確的位數"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message_auto))
            
    elif find_profile(user_id)["status"] == "start_play":
        computeranswer = find_game(user_id)["answer"]
        if userinput(message, computeranswer) == True:
            checking_answer = playgame(message, computeranswer)
            if checking_answer is None:
                delete_game(user_id)
                delete_profile(user_id)
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text = "恭喜答對!"))
            else:
                message_auto = "{}A{}B".format(checking_answer[0], checking_answer[1])
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message_auto))
        else:
            message_auto = "輸入正確答案(一到五位數)"
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text = message_auto))
#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)