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
	def __init__(self, pin, cls): # 押下時にclsクラスのpush_event()メソッドを実行する
--------------------
拡張
  - LED数の増加（プッシュボタンも増加してしまう -> ピン数が不足するか？）
  - スティック入力素子の追加（ボタンの増加を抑え、あるいはボタンを不要とし、使用するピン数を削減）
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
		self.b.when_pressed = cls.push_event
