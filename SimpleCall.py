from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der tollen Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
apiUrl = "https://webexapis.com/v1/xapi/command/dial"
access_token = os.getenv("ACCESSTOKEN")
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

body = {"deviceId" : "Y2lzY29zcGFyazovL3VybjpURUFNOnVzLWVhc3QtMl9hL0RFVklDRS80MTAyZjY0Zi0xMzE4LTQ3YjgtYmY3NC0wMjFkNzMyMDE2MGE","arguments": {"Number":"bjoern.engel@experteach.de"}}

response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

print(response.status_code)
print(response.text)