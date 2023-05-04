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