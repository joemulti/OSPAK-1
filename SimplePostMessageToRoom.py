from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

access_token = os.getenv("ACCESSTOKEN")
room_ID = os.getenv("ROOMID")

# Da wir eine Nachricht versenden wollen, hängen wir an die Funktionsurl /messages an
apiUrl = "https://api.ciscospark.com/v1/messages"

# Die Header Information wird gefüllt, sowie unser Access Token angehängt.
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

# Die Body Information wird gefüllt und der key 'text' mit einem Wert- unserer Nachricht befüllt
body = {"roomId" : room_ID, "text" : "Testnachricht"}

#Die Nachricht wird verschickt, und die Rückgabe wird in der Variable "response" gespeichert
response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

#Der Statuscode, sowie die Rückgabe wird auf dem Terminal ausgegeben.
print(response.status_code)
print(response.text)