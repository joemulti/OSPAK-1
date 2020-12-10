# SimpleCreateRoom
from dotenv import load_dotenv
load_dotenv()
import requests
import os
import json

# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.

def createRoom(roomprefix):

    apiUrl = "https://api.ciscospark.com/v1/rooms"
    access_token = os.getenv("ACCESSTOKEN")
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}

    body = {"title" : roomprefix + " Testraum WebexTeams API Kurs"}

    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

    data = json.loads(response.text)

    #print ('id : '+str(data['id']))
    #print ('title : ' + str(data['title']))
    
    return (str(data['id']),str(data['title']))