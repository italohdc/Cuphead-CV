from .template import ImageTemplate
from .yolo_prediction import YoloPrediction as Prediction
import torch
import cv2

class YoloDetection:
    def __init__(self, model_path: str = 'cuphead_model.pt'):
        self.model = torch.hub.load('ultralytics/yolov5', 'custom', path = model_path)
        pass

    def detect_single_image(self, image: ImageTemplate | cv2.Mat) -> Prediction:
        if isinstance(image, ImageTemplate):
            image_mat = image.get_template()
        else:
            image_mat = image

        prediction = self.model(image_mat, size=640)
        return Prediction(prediction)
