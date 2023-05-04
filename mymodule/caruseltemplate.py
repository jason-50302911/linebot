import re 
from linebot.models import *

def WantedCarouselTemplate(message):
    carousel_template_message = TemplateSendMessage(
        alt_text = '免費的影片',
        template = CarouselTemplate(
            columns = [
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/I4WfgZI.jpg',
                    tltle = '選單功能',
                    text = '想要什麼',
                    actions = [
                        MessageAction (
                                label = '所有貼圖',
                                text = '貼圖'
                            ),
                        MessageAction(
                            label = '所有地址',
                            text = '地址'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url = 'https://i.imgur.com/FgOTw9m.jpg',
                    tltle = '選單功能',
                    text = '想要什麼',
                    actions = [
                        MessageAction (
                            label = '所有圖片',
                            text = '所有圖片'
                        ),
                        MessageAction(
                            label = '多樣板組合',
                            text = '多樣板組合'
                        )
                    ]
                )
            ]
        )
    )
    return carousel_template_message






CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/VWcKhfR.jpg',
                        title = '選單功能',
                        text = '想要什麼',
                        actions = [
                            MessageAction (
                                label = '客製化選單',
                                text = '客製化選單'
                            ),
                            MessageAction(
                                label = '組圖訊息',
                                text = '組圖訊息'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/tANfcne.jpg',
                        tltle = '選單功能',
                        text = '想要什麼',
                        actions = [
                            MessageAction (
                            label = '小小影片',
                            text = '影片'
                            ),
                            MessageAction(
                                label = '大圖按鈕',
                                text = '大圖按鈕'
                            )
                        ]
                    )