from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json

messageID=os.getenv("MESSAGEID")


# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
apiUrl = "https://api.ciscospark.com/v1/messages/" + str(messageID)
access_token = os.getenv("ACCESSTOKEN")
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

body = {}

response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
data = json.loads(response.text)

print(response.status_code)
print(response.text)
print(data['text'])