from dotenv import load_dotenv
load_dotenv()
import json
import os
import requests

def recognize_face(pictureurl):
    subscription_key = os.getenv('FACE_SUBSCRIPTION_KEY')

    #face_api_url = os.getenv['FACE_ENDPOINT'] + '/face/v1.0/detect'
    face_api_url = 'https://webexdemo.cognitiveservices.azure.com/face/v1.0/detect'

    image_url = pictureurl

    headers = {'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'detectionModel': 'detection_01',
        'returnFaceAttributes': 'age,gender,smile,glasses,emotion',
        'returnFaceId': 'false'
    }

    response = requests.post(face_api_url, params=params,
                            headers=headers, json={"url": image_url})

    data=json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))
    return data