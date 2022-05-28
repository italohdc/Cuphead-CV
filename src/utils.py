from game_interface.window_capture import WindowCapture
from datetime import datetime

def save_screenshot_current_time(window: WindowCapture):
    if not isinstance(window, WindowCapture):
        raise Exception("window is not a WindowCapture object")

    time = datetime.now()
    time_string = time.strftime("cuphead-%m_%d_%Y-%H_%M_%S_%f")
    file = f'dataset/raw/{time_string}.png'
    window.save_screenshot(file)
    print('Saved screenshot to:', file)
