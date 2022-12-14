import re
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
line_bot_api = LineBotApi('4btdAHqOoEmk5RkZ8jh3UzVlJkdh6Y7LT+rKrJ5rfCYdXbMMm3Kkxnli5n27YbgLTZXGBaMYCGcQd0y8o2WbPO4rbOT+eosHRj9YS9aKN+iNhMJ5SvigCzNqefvLGrB9wvjnURhYg6OmN3PbzW5eJQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('9accd5784fbd1c1fa50b0b4cb2fe1d46')

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
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token, message
    message=text=event.message.text
    if re.match('hello', message):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='good morning'))
    else:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(message))

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
