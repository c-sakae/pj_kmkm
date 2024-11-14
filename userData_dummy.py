'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
====================
userData.py
====================
ユーザのデータを保持している。
インスタンス化は不要。

使用例：
	UserData.data[1]["led_pin"]で、
	uid = 1 のユーザに対応するLEDのピン番号を取得できる。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
class UserData:
	uids = [1, 2, 3]
	data = {
	    1:{"uid":1, "led_pin":XX,"button_pin":XX, "uname":"my name",  "line_uid":"my_LINE_ID"}, 
	    2:{"uid":2, "led_pin":XX,"button_pin":XX, "uname":"his name", "line_uid":"his_LINE_ID"}, 
	    3:{"uid":3, "led_pin":XX,"button_pin":XX, "uname":"her name", "line_uid":"her_LINE_ID"}
	}
