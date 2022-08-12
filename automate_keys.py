import keyboard

#nd= keyboard.record(until="esc")
#keyboard.play(nd,speed_factor=2)
keyboard.add_hotkey("a+s", lambda : keyboard.write("screenshot this page later"))
keyboard.wait("space")