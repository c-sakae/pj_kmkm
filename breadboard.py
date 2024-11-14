'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
====================
breadboard.py
====================
ブレッドボードとのやりとりを受け持つ。

--------------------
最初の目標
  - ブレッドボード上の素子：LED*3, button*3
----------
方針
  - Led, Buttonの２つのクラスを作成する。
  - 素子１つにつきインスタンスを１つ生成する。
----------
インターフェース
class Led:
	def __init__(self, pin):
	def on(self): # ledを点灯させるメソッド
	def off(self): # ledを消灯させるメソッド
class Button:
	def __init__(self, pin, cls): # 押下時にpush()メソッドを実行するようイベントを登録
--------------------
拡張
  - LEDをLCDに置き換え（可視性は低下するが、ユーザ数の変動に耐えられる。）
  - ボタン数を１〜２つに抑え、スティック入力素子を追加（ユーザ数の変動に耐えられる。）
--------------------
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
from gpiozero import Button as Btn
from gpiozero import LED

class Led:
	def __init__(self, pin):
		self.l = LED(pin)
		
	def on(self):
		self.l.on()
		
	def off(self):
		self.l.off()
		
class Button:
	def __init__(self, pin, cls):
		self.b = Btn(pin)
		self.b.when_pressed = self.pushed
		
		self.cls = cls
		self.pin = pin
		
	def pushed(self):
		# ここに処理を追加して、チャタリングを考慮したプログラムに変えたい。
		self.cls.push_event(self.pin)

