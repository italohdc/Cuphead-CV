import win32gui, win32ui, win32con
import numpy as np
import ctypes
import cv2

class WindowCapture:
    def __init__(self, window_name = "Cuphead"):
        # fix issue with Windows screen scale
        ctypes.windll.shcore.SetProcessDpiAwareness(2)

        # find the handle for the window we want to capture
        self.window = win32gui.FindWindow(None, window_name)
        self.screen = win32gui.GetDesktopWindow()
        if not self.window:
            raise Exception("Window not found. The game must be launched.")

        self.raise_window_to_foreground()
        self.update_window_dimensions()

    def update_window_dimensions(self):
        window_rect = win32gui.GetWindowRect(self.window)
        self.window_rect = window_rect
        self.w = window_rect[2] - window_rect[0]
        self.h = window_rect[3] - window_rect[1]

        # calculate game size and offset on the screen
        border_pixels = 9 # 8
        titlebar_pixels = 40 # 30
        black_bar_pixels = 21 # 10

        self.w = self.w - (border_pixels * 2)
        self.h = self.h - titlebar_pixels - border_pixels - (black_bar_pixels * 2)

        self.offset_x = window_rect[0] + border_pixels
        self.offset_y = window_rect[1] + titlebar_pixels + black_bar_pixels
    
    def raise_window_to_foreground(self):
        # raise window to the front (if possible)
        try:
            win32gui.SetForegroundWindow(self.window)
        except:
            print("Failed to set window to foreground")

    def get_screenshot(self) -> cv2.Mat:
        # update window dimensions and location
        self.update_window_dimensions()

        # get the window image data
        wDC = win32gui.GetWindowDC(self.screen)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, self.w, self.h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (self.w, self.h), dcObj, (self.offset_x, self.offset_y), win32con.SRCCOPY)

        # convert the raw data into a format opencv can read
        signedIntsArray = dataBitMap.GetBitmapBits(True)
        img = np.fromstring(signedIntsArray, dtype='uint8')
        img.shape = (self.h, self.w, 4)

        # free resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(self.window, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())

        # drop the alpha channel, or cv.matchTemplate() will throw an error like:
        #   error: (-215:Assertion failed) (depth == CV_8U || depth == CV_32F) && type == _templ.type() 
        #   && _img.dims() <= 2 in function 'cv::matchTemplate'
        img = img[...,:3]

        # make image C_CONTIGUOUS to avoid errors that look like:
        #   File ... in draw_rectangles
        #   TypeError: an integer is required (got type tuple)
        # see the discussion here:
        # https://github.com/opencv/opencv/issues/14866#issuecomment-580207109
        img = np.ascontiguousarray(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def show_screenshot(self, wait: int = 1, window_name: str = "Screenshot"):
        img = self.get_screenshot()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imshow(window_name, img)
        cv2.waitKey(wait)

    def save_screenshot(self, path = "screenshot.png"):
        img = self.get_screenshot()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        cv2.imwrite(path, img)

    def get_rect_borderless(self, box):
        # generate a new rect without borders and black bars
        new_box = (box[0] + self.offset_x, box[1] + self.offset_top, box[2] - self.offset_x, box[3] - self.offset_bottom)
        return new_box
