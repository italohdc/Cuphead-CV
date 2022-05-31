import torch
import cv2

class YoloPrediction:
    def __init__(self, prediction: torch.Tensor):
        self.prediction = prediction
        pass

    def get_prediction(self):
        return self.prediction

    def get_annotated_image(self):
        self.prediction.render()
        img = self.prediction.imgs[0]
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img

    def show(self, wait: int = 1, window_name: str = "YOLO"):
        img = self.get_annotated_image()
        cv2.imshow(window_name, img)
        cv2.waitKey(wait)
