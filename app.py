import base64
import cv2
from flask import Flask, request, jsonify
from src.main import Prediction

app = Flask(__name__)


# defining an endpoint for running inference on image
@app.route('/predict', methods=["POST"])
def predict():
    dict_to_return = {"person_count": "Exception Occurred"}
    try:
        json_data = request.get_json(force=True)  # getting the json data
        # getting the image data in base64 format
        image_data = json_data['image']

        # converting the base64 image data into bytes
        image = base64.b64decode(image_data, validate=True)

        # saving the image
        with open("saved_image.jpg", 'wb') as f:
            f.write(image)
            print("Image saved successfully\n")

            # reading the saved image
            frame = cv2.imread("images/saved_image.jpg", cv2.IMREAD_COLOR)

            # prediction object
            prediction_object = Prediction()

            # passing the image to yolov8 model
            person_count = prediction_object.count_person(frame)
            print(f"Number of percent count is: {person_count}")

            # returning the response
            dict_to_return['person_count'] = person_count
    except Exception as e:
        print(f"Exception: {e}")

    return jsonify(dict_to_return)


app.run()
