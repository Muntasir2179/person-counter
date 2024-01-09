import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/src/model/yolov8x.pt')


class Prediction:
    def __init__(self):
        self.model_path = "src/model/yolov8.pt"

    def count_person(self, frame):
        # Run YOLOv8 inference on the frame
        results = model.predict(source=frame, conf=0.5,
                                iou=0.6, classes=[0], imgsz=[640, 480])
        # Get the count of persons on the frame
        person_count = len(results[0])
        return person_count
