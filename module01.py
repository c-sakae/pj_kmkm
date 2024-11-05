'''
┌────────────────────────────────────┐
│breadboard担当者のためのテスト用プログラム│
└────────────────────────────────────┘
このモジュールを実行してちゃんと動けば、
ボタンについてはとりあえず正しくプログラムできていると思います。
'''
from breadboard import Button
from userData import UserData
from signal import pause

class Class01:
	def __init__(self, uid):
		udata = UserData()
		udata = udata.users[uid]
		self.uid = uid
		self.button = Button(udata["button_pin"], self)
	def push_event(self):
		print("pushed!")

user01 = Class01(1)
user02 = Class01(2)
user03 = Class01(3)

pause()
