from dotenv import load_dotenv
load_dotenv()
import requests
import os
#Zum Verarbeiten der JSON Daten
import json
import time

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

access_token = os.getenv("ACCESSTOKEN")
room_ID = os.getenv("ROOMID")

# Da wir eine Nachricht versenden wollen, hängen wir an die Funktionsurl /messages an
apiUrl = "https://api.ciscospark.com/v1/messages"

# Die Header Information wird gefüllt, sowie unser Access Token angehängt.
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

# Die Body Information wird gefüllt
body = {"roomId" : room_ID, "text" : "Testnachricht"}

#Die Nachricht wird verschickt, und die Rückgabe wird in der Variable "response" gespeichert
response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

#Der Statuscode, sowie die Rückgabe wird auf dem Terminal ausgegeben.
# print(response.status_code)
# print(response.text)

# der Rückgabetext wird zur weiteren Verarbeitung in ein Json Dict namens data überführt
data = json.loads(response.text)

#Wir geben die ID der Nachricht aus.
print (data['id'])
dataID=str(data['id'])

#Wir warten 5 Sekunden
time.sleep(5)
apiUrl = "https://api.ciscospark.com/v1/messages/" + dataID
body = {"text" : "Ich bin verändert"}

#Und löschen unsere Nachricht wieder
response = requests.put(url=apiUrl, json=body, headers=httpHeaders)
print (response.status_code)
print (response.text)
