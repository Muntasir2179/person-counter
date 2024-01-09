import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('/src/model/yolov8x.pt')


def count_from_image(frame):
    # Run YOLOv8 inference on the frame
    results = model.predict(source=frame, conf=0.5,
                            iou=0.6, classes=[0], imgsz=[640, 480])
    # Get the count of persons on the frame
    person_count = len(results[0])
    return person_count


if __name__ == "__main__":
    frame = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
    print(f"Number of percent count is: {count_from_image(frame)}")
    cv2.destroyAllWindows()
