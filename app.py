import os
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
app = Flask(__name__)
# Channel Access Token
line_bot_api = LineBotApi(
    'pHBOmN2+j++jFH0VrPsjl6cRb22qFRxVCjIkRzgKLWQtc+8eNGkdKY2eu80gRe9eOHbxSye/aGm5yD1JCvKFfXlhXGc3k5SICmEVWQlBppJP6m/BJAgPldPbveU4WRk6mGYaxohIEQSBnDBLnOq+wgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('86232b0516f94b4fde8a18712280d1f5')
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
# 處理訊息


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)


@app.route('/')
def index():
    return 'Hello World'


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    app.run(host='0.0.0.0', port=port)
