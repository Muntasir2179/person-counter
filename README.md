# Person Counter
This repository is created to work on a simple API of a machine learning model. The model ran inference on an image to count the number of person. We have defined endpoints which can be used to pass an image in base64 format and the API will send a response containing the person count in that image.

## Installation
After installing required pacages ran the app.py file. Then you can send request to the endpoint `/predict`.
```sh
pip install -r requirements.txt
```


## How to make a request
In order to get an appropriate reasponse you have to pass a json data as a key value pair. You have to send a `POST` request to the endpoint `/predict` with the json data in following format. Use [Base64 Image Encoder](https://www.base64-image.de/) to serialize the image before sending the request.

```
{
    "image": "base64_image_data"
}
```

## Response
The api will convert the base64 data into a frame and it will run inference. The api will send a json response containing the person count in the following format.
```
{
    "person_count": number of person
}
```