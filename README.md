# Person Counter
This repository is created to work on a simple API of a machine learning model. The model ran inference on an image to count the number of person. We have defined endpoints which can be used to pass an image in base64 format and the API will send a response containing the person count in that image.

## Installation
After installing required pacages ran the app.py file. Then you can send request to the endpoint `/predict`.
```sh
pip install -r requirements.txt
```

## NOTE
> Use [Base64 Image Encoder](https://www.base64-image.de/) to serialize the image before sending the request.
