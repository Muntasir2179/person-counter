import cv2
import time
from src.main import Prediction
from mysql_data_insertion import insert_into_database

prediction_object = Prediction()


def capture_frames():
    cap = cv2.VideoCapture(0)  # capture the camera video

    start_time = time.time()  # start the timer

    while cap.isOpened():
        success, frame = cap.read()  # read a frame

        # check if 10 second is complete or not
        if success and (time.time() - start_time >= 10):
            person_count = prediction_object.count_person(
                frame=frame)  # passing the frame into the model
            print(f"Number of person is: {person_count}")
            insert_into_database(person_count)
            start_time = time.time()  # reset the timer

        cv2.imshow('Camera Feed', frame)  # displaying the camera feed
        if cv2.waitKey(1) & 0xFF == ord('q'):  # setting q as a quit button
            break


if __name__ == "__main__":
    capture_frames()
