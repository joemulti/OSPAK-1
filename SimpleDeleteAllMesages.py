# Das Script holt sich die Nachrichten eines Raumes (50 per Default) und löscht diese - Hierzu ist allerdings das "ProPack", da hier ein User mit Compliance Rechten notwendig ist.
from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json



# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
roomId=os.getenv("ROOMID")
apiUrl = "https://api.ciscospark.com/v1/messages?roomId="+roomId
access_token = os.getenv("ACCESSTOKEN")
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
body = {}
# Nachdem wir die Get Nachrichteninhalte zusammengefügt haben, senden wir das GET los und speichern die Rückgabe ind der Variable Response
response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
data = json.loads(response.text)

# print(response.status_code)
# print(response.text)
# print(data)

#print (type(data))

for key in data['items']:
    datablock=str(key['id'])
    apiUrl = "https://api.ciscospark.com/v1/messages/" + datablock
    response = requests.delete(url=apiUrl, json=body, headers=httpHeaders)
    print (response.status_code)





