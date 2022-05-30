from game_interface.window_capture import WindowCapture
from datetime import datetime
import time
import utils

window_capture = WindowCapture("Cuphead")
time.sleep(1)

while True:
    start = datetime.now()

    screenshot = window_capture.get_screenshot()
    # utils.save_screenshot_current_time(window_capture)

    fps = 1 / (datetime.now() - start).total_seconds()
    time.sleep(0.1)
    print(f"FPS: {fps}")
