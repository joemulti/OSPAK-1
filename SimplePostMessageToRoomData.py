from dotenv import load_dotenv
load_dotenv()
import requests
import os
#Zum Verarbeiten der JSON Daten
import json

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

access_token = os.getenv("ACCESSTOKEN")
room_ID = os.getenv("ROOMID")

# Da wir eine Nachricht versenden wollen, hängen wir an die Funktionsurl /messages an
apiUrl = "https://api.ciscospark.com/v1/messages"

# Die Header Information wird gefüllt, sowie unser Access Token angehängt.
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

# Die Body Information wird gefüllt
body = {"roomId" : room_ID, "text" : "Ich bin die alternative Nachricht"}

#Die Nachricht wird verschickt, und die Rückgabe wird in der Variable "response" gespeichert
response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

#Der Statuscode, sowie die Rückgabe wird auf dem Terminal ausgegeben.
print(response.status_code)
print('Unformatierte Rückgabe: '+ response.text)
print (type(response.text))
# der Rückgabetext wird zur weiteren Verarbeitung in ein Json Dict namens data überführt
data = json.loads(response.text)
print (type(data))
#Wir geben die ID der Nachricht aus.
print ('Der Inhalt des Key "id": '+ data['id'])
print ('Der Inhalt des Key "text": '+data['text'])

# Die Body Information wird gefüllt
body = {"roomId" : room_ID, "text" : 'Der Neue Aufruf des Key "text": '+data['text'] }
response = requests.post(url=apiUrl, json=body, headers=httpHeaders)