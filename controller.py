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
ひとこと
  - インスタンスはapp.pyにて保持されるので、ひとまず入室状況などをファイル出力せずフィールド(self.変数名)に置いておいても機能する。
----------
機能
  - スイッチが押されると、入室状況を変更し、LEDを更新する。
  - LINEからメッセージが送られると、入室状況を書き出す。
----------
インターフェース
class Controller:
	def __init__(self): # プロダクト起動時にapp.pyにて実行される。
	def respMsgEvnt(self, reqtext): # LINEへの応答メッセージをreturnするメソッド。reqtext: LINEからメッセージ
class XXX: # breadboardモジュールのButtonクラスにclsとして渡すクラス。もちろんControllerと一緒コタでも可。
	def push_event(self):
-----------------------------------------------'''
#'''
class Controller:
	def __init__(self):
		pass

	def respMsgEvnt(self, reqtext):
		resptext = reqtext
		# 処理
		return resptext
	
class XXX:
	def push_event(self):
		pass
		
#'''
