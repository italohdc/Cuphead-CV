from game_interface.window_capture import WindowCapture
from game_interface.handle_action import HandleAction, Action
import time

window_capture = WindowCapture("Cuphead")
time.sleep(1)

HandleAction.hold(Action.SHOOT)

while True:
    window_capture.show_screenshot()
    HandleAction.execute(Action.JUMP)
