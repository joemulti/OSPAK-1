from dotenv import load_dotenv
load_dotenv()
import requests
import os 

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
apiUrl = "https://api.ciscospark.com/v1/webhooks/"+os.getenv("WEBHOOKID")
print (apiUrl)
access_token = os.getenv("ACCESSTOKEN")
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
response = requests.delete(url=apiUrl, headers=httpHeaders)

print(response.status_code)
print(response.text)