import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
from PIL import Image
import requests
import io

#Loading the pre-trained model
model = MobileNetV2(weights='imagenet')


def analyze_image(img):
    img_array = preprocess_input(np.expand_dims(image.img_to_array(img), axis=0))
    preds = model.predict(img_array)
    decoded_preds = decode_predictions(preds, top=3)[0] 
    return [{'Element Name: ': pred[1], 'confidence':  round(float(pred[2]), 3)} for pred in decoded_preds]
    

def classify_image(image_data):
    """Classify an image by analyzing filepath or a url"""
    # Opening file by checking if the image_data is URL or a file object.
    if isinstance(image_data, str):  
        response = requests.get(image_data)
        img = Image.open(io.BytesIO(response.content)).resize((224, 224))
    else:  
        img = Image.open(io.BytesIO(image_data.read())).resize((224, 224))

    # Analyze the image using pre-trained model
    analysis = analyze_image(img)

    #setting url or filename for the return response
    if isinstance(image_data, str):
        image_info = {'Image_url': image_data}
    else:
        image_info = {'Image': image_data.filename}

    return {**image_info, 'analysis': analysis}


