from game_interface.window_capture import WindowCapture
from datetime import datetime

def get_string_datetime_now():
    time = datetime.now()
    time_string = time.strftime("%Y_%m_%d-%H_%M_%S_%f")
    return time_string

def save_screenshot_current_time(window: WindowCapture):
    if not isinstance(window, WindowCapture):
        raise Exception("window is not a WindowCapture object")

    time = get_string_datetime_now()
    file = f'dataset/raw/{time}.png'
    window.save_screenshot(file)
    print('Saved screenshot to:', file)
