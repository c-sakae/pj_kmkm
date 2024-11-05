"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
====================
app.py
====================
line-bot-sdk(python)の公式サイトより、Synopsisをほぼ丸コピ。
概要：
	- Webサーバに相当する（？）。
		scr_flask.shにて、flask run するときにimportされるファイルである。
	- "/"にGETがrequestされると、文字列（htmlドキュメント？）を返す。
	- "/callback"にMessaginAPIのメッセージrequestがPOSTされると、
		Appサーバに相当する（？）callbackモジュールにcallbackし、
		受け取った文字列をresponseとして返す。
	- シェルでpython app.pyを実行すると、ポート5100を使用する。
処理順：
	1. import
	2. インスタンス化
	3. flaskのルーティングの記述
	4. linebotのイベントハンドラの記述
	5. Flask.run()
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#--------------------------------------------------
#import part
from flask import Flask, request, abort
from auth import LineAuth
from controller import Controller

from linebot.v3 import (
    WebhookHandler
)
from linebot.v3.exceptions import (
    InvalidSignatureError
)
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
from linebot.v3.webhooks import (
    MessageEvent,
    TextMessageContent
)
#--------------------------------------------------
#instance-creating part
app = Flask(__name__)
ctrl = Controller()

line_auth = LineAuth()
configuration = Configuration(access_token=line_auth.access_token)
handler = WebhookHandler(line_auth.secret)
del line_auth
#--------------------------------------------------
#flask routing
@app.route("/")
def hello_world():
	return "<head><title>IoT Project</title></head><p>グループ３！</p>"

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
        app.logger.info("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

#--------------------------------------------------
#linebot event handler
@handler.add(MessageEvent, message=TextMessageContent)
def handle_message(event):
    with ApiClient(configuration) as api_client:
        line_bot_api = MessagingApi(api_client)
        line_bot_api.reply_message_with_http_info(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[TextMessage(text=ctrl.respMsgEvnt(event.message.text))]
            )
        )
#--------------------------------------------------
#Flask.run() part
if __name__ == "__main__":
    app.run(port=5100)
#--------------------------------------------------
