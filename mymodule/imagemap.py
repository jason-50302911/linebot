import re
from linebot.models import *

def WantedImagemap(message):
    if re.match('組圖訊息', message):
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
            return imagemap_message