'''
testing controller.py

command:
sudo ~/davinci-kit-for-raspberry-pi/pj_kmkm/venv/bin/python ~/davinci-kit-for-raspberry-pi/pj_kmkm/module02.py

press ctr+C to quit
'''
import controller
import keyboard
from signal import pause

ctlr = controller.Controller()

def action():
	print("sending text")
	text = input()
	print("source")
	source = input()
	return ctlr.respMsgEvnt(text, source)


keyboard.on_press_key(
	"a",
	lambda _: print(
		"\n" +
		action()
	)
)

pause()
