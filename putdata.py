 message = text = event.message.text
    if re.match('所有分類', message):
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
                                    label = '貼圖',
                                    text = '貼圖'
                                ),
                            MessageAction(
                                label = '地址',
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
                                label = '圖片',
                                text = '圖片'
                            ),
                            MessageAction(
                                label = '選擇按鍵',
                                text = '選擇按鍵'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url = 'https://i.imgur.com/VWcKhfR.jpg',
                        tltle = '選單功能',
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
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, carousel_template_message)
    elif re.match('貼圖', message):
        sticker_message = StickerSendMessage(
            package_id = '446',
            sticker_id = '1990'
        )
        line_bot_api.reply_message(event.reply_token, sticker_message)
    elif re.match('地址', message):
        location_message = LocationSendMessage(
            title = '高雄的學校',
            address = '我的學校',
            latitude = 22.78757415480277,
            longitude = 120.40710230230081
        )
        line_bot_api.reply_message(event.reply_token, location_message)
    elif re.match('大圖按鈕', message):
        image_carousel_message = TemplateSendMessage(
            alt_text = '我看不到',
            template = ImageCarouselTemplate(
                columns = [
                    ImageCarouselColumn(
                        image_url = 'https://i.imgur.com/I4WfgZI.jpg',
                        action = PostbackAction(
                            label = '我教你武功',
                            display_text = '所有分類',
                            data = 'Are You Sure'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url = 'https://imgur.com/o8F1E49.jpg',
                        action = MessageAction(
                            label = '我操',
                            text = '所有分類'
                        )
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, image_carousel_message)
    elif re.match('客製化選單', message):
        flex_message = FlexSendMessage(
            alt_text = '我的專頁',
            contents = {
                "type": "bubble",
                "body": {
                    "type": "box",
                    "layout": "vertical",
                    "contents": [
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "image",
                            "url": "https://i.imgur.com/xRhHK27.jpg",
                            "size": "5xl",
                            "aspectMode": "cover",
                            "aspectRatio": "150:196",
                            "gravity": "center",
                            "flex": 1
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/tANfcne.jpg",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "150:98",
                                "gravity": "center"
                            },
                            {
                                "type": "image",
                                "url": "https://i.imgur.com/zRf4ayR.jpg",
                                "size": "full",
                                "aspectMode": "cover",
                                "aspectRatio": "150:98",
                                "gravity": "center"
                            }
                            ],
                            "flex": 1
                        }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "horizontal",
                        "contents": [
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "image",
                                "url": "https://scdn.line-apps.com/n/channel_devcenter/img/flexsnapshot/clip/clip13.jpg",
                                "aspectMode": "cover",
                                "size": "full"
                            }
                            ],
                            "cornerRadius": "100px",
                            "width": "80px",
                            "height": "80px"
                        },
                        {
                            "type": "box",
                            "layout": "vertical",
                            "contents": [
                            {
                                "type": "text",
                                "contents": [
                                {
                                    "type": "span",
                                    "text": "Sexy_dessert",
                                    "weight": "bold",
                                    "color": "#000000",
                                    "size": "lg"
                                },
                                {
                                    "type": "span",
                                    "text": "     "
                                },
                                {
                                    "type": "span",
                                    "text": "I just want to eat lots of dessert and take great picture inTaiwan"
                                }
                                ],
                                "size": "sm",
                                "wrap": True
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "contents": [
                                {
                                    "type": "text",
                                    "text": "777,777,777 Like",
                                    "size": "sm",
                                    "color": "#bcbcbc"
                                }
                                ],
                                "spacing": "sm",
                                "margin": "md"
                            }
                            ]
                        }
                        ],
                        "spacing": "xl",
                        "paddingAll": "20px"
                    }
                    ],
                    "paddingAll": "0px"
                }
            }
        )
        line_bot_api.reply_message(event.reply_token, flex_message)
    elif re.match('影片', message):
        video_message = VideoSendMessage(
            original_content_url= 'https://imgur.com/G7MgBG0.mp4',
            preview_image_url = 'https://imgur.com/JliRzrH.jpg',
            durtion = 1500
        )
        line_bot_api.reply_message(event.reply_token, video_message)
    elif re.match('組圖訊息', message):    
        imagemap_message =  ImagemapSendMessage(
            base_url = 'https://i.imgur.com/I4WfgZI.jpg',
            alt_text = 'This is an imagemap',
            base_size = BaseSize(height = 1040, width = 1040),
            video = Video(
                original_content_url = 'https://imgur.com/6HXxoht.mp4',
                preview_image_url = 'https://imgur.com/JliRzrH.jpg',
                area = ImagemapArea(
                    x = 0, y = 0, width = 1040, height = 585
                ),
                external_link = ExternalLink(
                    link_uri = 'https://www.amazon.com',
                    label = '查看更多....',
                ),    
            ),
            actions = [
                URIImagemapAction(
                    link_uri = 'https://www.instagram.com/kingpa_op/',
                    area = ImagemapArea(
                        x = 0, y = 0, width = 520, height = 1040
                    ),
                ),
                MessageImagemapAction(
                    text = '戳我幹嘛',
                    area = ImagemapArea(
                        x = 520, y = 0, width = 520, height = 1040
                    )
                )
            ]
        )
        line_bot_api.reply_message(event.reply_token, imagemap_message)
    elif re.match('選擇按鍵', message):
        confirm_Template_message = TemplateSendMessage(
            alt_text = '問你小問題',
            template = ConfirmTemplate(
                text = 'ARE YOU SURE?',
                actions = [
                    PostbackAction(
                        label = 'LIKE',
                        display_text = '所有分類',
                        data = 'action = DO NOT REALLY LIKE'
                    ),
                    PostbackAction(
                        label = 'BAD',
                        display_text = '所有分類',
                        data = 'SUPER BAD'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, confirm_Template_message)
    elif re.match('圖片', message):
        image_message = ImageSendMessage(
            original_content_url = 'https://imgur.com/JliRzrH.jpg',
            preview_image_url = 'https://imgur.com/JliRzrH.jpg'
        )
        line_bot_api.reply_message(event.reply_token, image_message)
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))