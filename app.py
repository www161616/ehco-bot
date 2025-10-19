# -*- coding: utf-8 -*-
from flask import Flask, request, abort
import json
from urllib.parse import quote

from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TemplateMessage,
    ButtonsTemplate,
    ImageCarouselTemplate,
    ImageCarouselColumn,
    MessageAction,
    URIAction,
    FlexMessage,
    FlexContainer,
    VideoMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent,
)

# --- 從 flex_messages.py 引入所有地區的 JSON 資料 ---
from flex_messages import (
    taipei_stores_json,
    new_taipei_stores_json_1,
    new_taipei_stores_json_2,
    taoyuan_stores_json,
    hsinchu_stores_json
)


app = Flask(__name__)

# --- 您的 Channel Access Token ---
ACCESS_TOKEN = 'tAXUd2NwWXN90k6Kg1067PUce+C42Wqw9KmkCV/U+X0kmPPOD1HPudvopjaD2QYen8mWzwF9vjDiXsC1oJ4Ag0LHjcG6MPDW7UNQfEzkRzjrp2Xf/tnnVlj/9SWmCyPc2Nr22pK6i82h8CiX6tnbKAdB04t89/1O/w1cDnyilFU='
# --- 您的 Channel Secret ---
CHANNEL_SECRET = 'b72e8b0a3f00beeaaf31d1e09ce9f081'

configuration = Configuration(access_token=ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    except Exception as e:
        app.logger.error(f"Error handling webhook: {e}")
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    text = event.message.text.strip()
    
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)

        # --- 門市總查詢按鈕 ---
        if text == '門市查詢':
            try:
                image_url = "https://i.meee.com.tw/cnGnZpJ.png"
                buttons_template = ButtonsTemplate(
                    thumbnail_image_url=image_url,
                    title='選擇分店',
                    text='請選擇離您最近的區域',
                    actions=[
                        MessageAction(label='台北區', text='台北分店'),
                        MessageAction(label='新北區', text='新北分店'),
                        MessageAction(label='桃園區', text='桃園分店'),
                        MessageAction(label='新竹區', text='新竹分店')
                    ]
                )
                template_message = TemplateMessage(alt_text="門市查詢", template=buttons_template)
                line_bot_api.reply_message(
                    ReplyMessageRequest(reply_token=event.reply_token, messages=[template_message])
                )
            except Exception as e:
                app.logger.error(f"An error occurred when replying to '門市查詢': {e}")

        # --- 各地區分店查詢 ---
        elif text == '台北分店':
            try:
                flex_content = json.loads(taipei_stores_json)
                flex_message = FlexMessage(alt_text='台北區分店資訊', contents=FlexContainer.from_dict(flex_content))
                line_bot_api.reply_message(ReplyMessageRequest(reply_token=event.reply_token, messages=[flex_message]))
            except Exception as e:
                app.logger.error(f"Error sending Taipei Flex Message: {e}")

        elif text == '新北分店':
            try:
                flex_content_1 = json.loads(new_taipei_stores_json_1)
                flex_message_1 = FlexMessage(alt_text='新北區分店資訊(1)', contents=FlexContainer.from_dict(flex_content_1))
                flex_content_2 = json.loads(new_taipei_stores_json_2)
                flex_message_2 = FlexMessage(alt_text='新北區分店資訊(2)', contents=FlexContainer.from_dict(flex_content_2))
                line_bot_api.reply_message(ReplyMessageRequest(reply_token=event.reply_token, messages=[flex_message_1, flex_message_2]))
            except Exception as e:
                app.logger.error(f"Error sending New Taipei Flex Messages: {e}")

        elif text == '桃園分店':
            try:
                flex_content = json.loads(taoyuan_stores_json)
                flex_message = FlexMessage(alt_text='桃園區分店資訊', contents=FlexContainer.from_dict(flex_content))
                line_bot_api.reply_message(ReplyMessageRequest(reply_token=event.reply_token, messages=[flex_message]))
            except Exception as e:
                app.logger.error(f"Error sending Taoyuan Flex Message: {e}")
        
        elif text == '新竹分店':
            try:
                flex_content = json.loads(hsinchu_stores_json)
                flex_message = FlexMessage(alt_text='新竹區分店資訊', contents=FlexContainer.from_dict(flex_content))
                line_bot_api.reply_message(ReplyMessageRequest(reply_token=event.reply_token, messages=[flex_message]))
            except Exception as e:
                app.logger.error(f"Error sending Hsinchu Flex Message: {e}")

        # --- 進入團購 (已修正為您的公開圖片與連結) ---
        elif text == '進入團購':
            try:
                app.logger.info("Matched keyword: 進入團購")
                image_carousel_template = ImageCarouselTemplate(
                    columns=[
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/ZqhQRfX.jpg', action=URIAction(label='按此進入1群', uri='https://line.me/ti/g2/MUGYiLc70g5E8_BX8D0dMqOnlktIfKg_M__Alw?utm_source=invitation&utm_medium=link_copy&utm_campaign=default')),
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/GSVDHeq.jpg', action=URIAction(label='進入靜悄悄群', uri='https://line.me/ti/g2/iIJT05Zt6uqjjzADbiIOz_FXpFZkl4T5WV7PWQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default')),
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/IvxDRYT.jpg', action=URIAction(label='進入3群', uri='https://line.me/ti/g2/gbzMKBAEY0zOV97dtNumPlgGAoDd2MW5oqm1sQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default')),
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/Ddy4MTo.jpg', action=URIAction(label='進入南平店', uri='https://line.me/ti/g2/m4swh-R5grJcDg3QDo6uvZbmof3VGEtmpVbktg?utm_source=invitation&utm_medium=link_copy&utm_campaign=default')),
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/P6HNjxW.jpg', action=URIAction(label='進入三峽店', uri='https://line.me/ti/g2/01G_zHJYzMBZis49Ja1Xpc-yWWvE1M_ktKENkA?utm_source=invitation&utm_medium=link_copy&utm_campaign=default')),
                        ImageCarouselColumn(image_url='https://i.meee.com.tw/t84CUZ0.jpg', action=URIAction(label='進入經國店', uri='https://line.me/ti/g2/0Eldwi0Zy2lJ6G3hZI_mbFk87fJHB7_P02UpcQ?utm_source=invitation&utm_medium=link_copy&utm_campaign=default'))
                    ]
                )
                image_carousel_message = TemplateMessage(alt_text='進入團購群組', template=image_carousel_template)
                line_bot_api.reply_message(
                    ReplyMessageRequest(reply_token=event.reply_token, messages=[image_carousel_message])
                )
                app.logger.info("Image Carousel sent successfully.")
            except Exception as e:
                app.logger.error(f"An error occurred when replying to '進入團購': {e}")
        
        # --- 最新動態 ---
        elif text == '最新動態':
            try:
                app.logger.info("Matched keyword: 最新動態")
                video_message = VideoMessage(
                    original_content_url="https://raw.githubusercontent.com/www161616/photo/main/tik01.mp4",
                    preview_image_url="https://raw.githubusercontent.com/www161616/photo/main/tik01.png"
                )
                buttons_template = ButtonsTemplate(
                    title='觀看更多影片',
                    text='點擊下方按鈕，前往我們的 TikTok 主頁！',
                    actions=[
                        URIAction(label='前往我們的 TikTok', uri='https://www.tiktok.com/@pang_bao_zi?_t=ZS-90cCxpbpGNT&_r=1')
                    ]
                )
                template_message = TemplateMessage(alt_text="最新動態影片", template=buttons_template)
                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[video_message, template_message]
                    )
                )
                app.logger.info("Video and TikTok button sent successfully.")
            except Exception as e:
                app.logger.error(f"An error occurred when replying to '最新動態': {e}")


if __name__ == "__main__":
    app.run(port=5000)

