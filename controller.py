"""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
====================
controller.py
====================
概要：
	- Appサーバに相当する（？）。
		Controllerクラスはapp.py実行時にインスタンス化され、イベントハンドラによってrespMsgEvnt()が呼び出される。
	- Raspberry Piに接続したブレッドボードを使うときは、breadboardに仲介してもらう。
アプリ１（parroting）：
	- オウム返しに答えるソフト。
アプリ２（ledOnOff）：
	- テキストでLEDのON,OFFを制御するソフト。
アプリ３（accessControl）：
	- 入室管理ソフト
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
#--------------------------------------------------
#parroting
# LINEメッセージに対し、オウム返しに答えるソフト
# 回答内容を別モジュールで生成するため、最初に制作したもの。
# 実装すべき関数は、__init__(), respMsgEvnt() の２つ。
"""
class Controller:
	def __init__(self):
		pass
	def respMsgEvnt(self, reqtext):
		return reqtext
"""
#--------------------------------------------------
#ledOnOff
# LINEメッセージで、LEDのON,OFFを制御するソフト。
# breadboardモジュール担当者のために試作。
# LEDのチュートリアル通り、17ピンにLEDが接続されている想定。
'''-----------------------------------------------
  - (例)命令: 実行内容
  - "turn on": LEDを点灯させる。
  - "turn off"： LEDを消灯させる。
  - "check"： LEDの状態（点灯・消灯）を回答する。
  - その他： 定義済みの（上の３つの）命令でない旨を回答する。
-----------------------------------------------'''
'''
from breadboard import Led

class Controller:
	def __init__(self):
		self.led = Led(17)

	def respMsgEvnt(self, reqtext):
		resptext = "wrong output"

		if (reqtext=="turn on"):
			self.led.on()
			resptext = "turned on"
		elif (reqtext=="turn off"):
			self.led.off()
			resptext = "turned off"
		elif (reqtext=="check"):
			isOn = self.led.check()
			if (isOn == True):
				resptext = "it is on"
			elif (isOn == False):
				resptext = "it is off"
			else:
				resptext = "failed to check"
		else:
			resptext = "undefined order"

		return resptext
'''
#--------------------------------------------------
#accessControl
'''-----------------------------------------------
機能
  - スイッチが押されると、入室状況を変更し、LEDを更新する。
  - LINEからメッセージが送られると、入室状況を書き出す。
----------
インターフェース
class Controller:
	def __init__(self): # プロダクト起動時にapp.pyにて実行される。
	def respMsgEvnt(self, reqtext): # LINEへの応答メッセージをreturnするメソッド。reqtext: LINEからメッセージ
	def push_event(self, pin): # breadboard.Buttonインスタンスに登録するイベント
-----------------------------------------------'''
#'''
from userData import UserData as ud
import breadboard

class Controller:
	def __init__(self):
		'''
		３つのフィールドを初期化
		'''
		self.led = {}
		self.btn = {}
		self.isIn = {}
		for uid in ud.uids:
			self.led[uid]  = breadboard.Led   (ud.data[uid]["led_pin"]         )
			self.btn[uid]  = breadboard.Button(ud.data[uid]["button_pin"], self)
			self.isIn[uid] = False

	def respMsgEvnt(self, reqtext, source_id):
		'''
		LINEからのメッセージに対するアクション
		引数：
			reqtext: メッセージ（文字列）
			source_id: メッセージの送り主（source）のLINE_ID（文字列）
		アクションの内容：
			1. 認証。LINE_IDが未登録だった場合、IDを通知する。
			2. メッセージに従った処理
				- メッセージが "who's in?"
					- 入室状況を返却
				- メッセージが "log"
					- 入退室ログを返却
				- その他
					- 未定義のメッセージである旨の通知
		'''
		# 認証
		userid = -1
		for uid in ud.uids:
			if ud.data[uid]["line_uid"] == source_id:
				userid = uid
				break
		if userid == -1:
			return "Your line uid\n" + source_id + "\nis not registered."
		# メッセージの返却
		if reqtext == "who's in?":
			return self.respWhoIsIn()
		elif reqtext == "log":
			return "not alreadly implemented"
		else:
			return "an undefined order"

	def respWhoIsIn(self):
		'''
		入室状況（self.isIn）を文字列化して返すメソッド
		'''
		resptext = ""
		for uid in ud.uids:
			resptext += ud.data[uid]["uname"]
			resptext += " is "
			if (self.isIn[uid]):
				resptext += "in"
			else:
				resptext += "out"
			resptext += "\n"
		return resptext.rstrip("\n")

	def push_event(self, pin):
		'''
		ボタンが押されたときに発生するイベント。
		入室状態・退室状態（self.isIn）を切り替え、LEDの点灯・消灯を更新する。
		引数：
			pin: 押されたボタンのピン番号
		'''
		# pinに対応するユーザを探索
		uid = -1
		for userid in ud.uids:
			if pin == ud.data[userid]["button_pin"]:
				uid = userid
				break
		# イベント処理
		if uid == -1:
			# ユーザー登録されていないボタンが押されたとき
			pass
		elif self.isIn[uid] == True:
			# 入室 → 退室
			self.led[uid].off()
			self.isIn[uid] = False
		elif self.isIn[uid] == False:
			# 退室 → 入室
			self.led[uid].on()
			self.isIn[uid] = True
		else:
			# self.isInに正常な値が格納されていないとき
			pass
			
#'''
