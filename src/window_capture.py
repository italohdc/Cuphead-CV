from PIL import ImageGrab
import win32gui
import numpy as np
import ctypes
import cv2

class WindowCapture:
    def __init__(self, window_name = "Cuphead"):
        # fix issue with Windows screen scale
        ctypes.windll.shcore.SetProcessDpiAwareness(2)

        # find the handle for the window we want to capture
        self.window = win32gui.FindWindow(None, window_name)
        if not self.window:
            raise Exception("Window not found")

        # raise window to the front (if possible)
        try:
            win32gui.SetForegroundWindow(self.window)
        except:
            print("Failed to set window to foreground")

        # calculate the offsets to remove the borders
        border_pixels = 9
        titlebar_pixels = 40
        black_bars = 22

        self.offset_x = border_pixels
        self.offset_top = titlebar_pixels + black_bars
        self.offset_bottom = border_pixels + black_bars


    def get_screenshot(self):
        bbox = win32gui.GetWindowRect(self.window)
        bbox_borderless = self.get_rect_borderless(bbox)
        img = ImageGrab.grab(bbox_borderless)
        img_np = np.array(img.getdata(), dtype = 'uint8').reshape((img.size[1], img.size[0], 3))

        return img_np

    def show_screenshot(self):
        img = self.get_screenshot()
        img_cv = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow("demo", img_cv)
        cv2.waitKey(100)

    def get_rect_borderless(self, box):
        # generate a new rect without borders and black bars
        new_box = (box[0] + self.offset_x, box[1] + self.offset_top, box[2] - self.offset_x, box[3] - self.offset_bottom)
        return new_box
