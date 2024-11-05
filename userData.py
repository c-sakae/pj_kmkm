'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
====================
userData.py
====================
ユーザのデータを保持している。

使用例：
UserData.users[1]["led_pin"]で、
uid = 1 のユーザに対応するLEDのピン番号を取得できる
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
class UserData:
	def __init__(self):
		user01 = {"uid":1, "led_pin":17,"button_pin":25}
		user02 = {"uid":2, "led_pin":27,"button_pin":12}
		user03 = {"uid":3, "led_pin":26,"button_pin":21}
		self.users = [0, user01, user02, user03]
