from game_interface.window_capture import WindowCapture
from feature_detection.yolo import YoloDetection
from datetime import datetime
import time

yolo = YoloDetection()
window_capture = WindowCapture("Cuphead")
time.sleep(1)

while True:
    start = datetime.now()

    screenshot = window_capture.get_screenshot()
    prediction = yolo.detect_single_image(screenshot)
    prediction.show()

    fps = 1 / (datetime.now() - start).total_seconds()
    print(f"FPS: {fps}")
