from typing import List
from .template import ImageTemplate, MultipleImageTemplate
import cv2

class SingleMatch:
    def __init__(self, image: ImageTemplate, template: ImageTemplate, top_left, confidence):
        self.image = image
        self.template = template
        self.confidence = confidence

        template_mat = template.get_template()
        self.width = template_mat.shape[1]
        self.height = template_mat.shape[0]
        self.top_left = top_left
        self.bottom_right = (top_left[0] + self.width, top_left[1] + self.height)
    
    def get_image(self):
        img_mat = self.image.get_template()
        result_img = img_mat.copy()
        cv2.rectangle(result_img, self.top_left, self.bottom_right, 
            color=(0, 255, 0), thickness=2, lineType=cv2.LINE_4)
        return result_img

    def show(self, wait: int = 0, window_name: str = "SingleMatch"):
        img = self.get_image()
        cv2.imshow(window_name, img)
        cv2.waitKey(wait)
    
    def save_screenshot(self, path = "screenshot.png"):
        img = self.get_image()
        cv2.imwrite(path, img)

class Single:
    def __init__(self, image: ImageTemplate, template: ImageTemplate):
        self.image = image
        self.template = template

class MultipleMatch:
    def __init__(self, single_matches: List[SingleMatch], image: ImageTemplate, template: MultipleImageTemplate):
        self.single_matches = single_matches
        self.image = image
        self.template = template
