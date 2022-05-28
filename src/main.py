from game_interface.window_capture import WindowCapture
import time
import utils

window_capture = WindowCapture("Cuphead")
time.sleep(1)

while True:
    utils.save_screenshot_current_time(window_capture)
    time.sleep(0.1)

