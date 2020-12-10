from dotenv import load_dotenv
load_dotenv()
import requests
import os 
import json
import initLab
# Das Script arbeitet mit der Library "requests". Gegebenenfalls muss diese mit "pip install requests" nachinstalliert werden.
#apiUrl = "https://api.ciscospark.com/v1/webhooks/"+os.getenv("WEBHOOKID")
#print (apiUrl)

#httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
#response = requests.delete(url=apiUrl, headers=httpHeaders)

#print(response.status_code)
#print(response.text)

#def deleteWebhooks():

def listRooms():
    access_token = os.getenv("ACCESSTOKEN")
    apiUrl = "https://api.ciscospark.com/v1/rooms"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    response = requests.get(url=apiUrl, headers=httpHeaders)
    data=json.loads(response.text)
    i=1

    for id in data['items']:
        if str(os.getenv("CLASSPREFIX")) in str(id['title']):
            print ('Raum ' + str(i) + ' : '+ str(id['title']))
            i+=1

def deleteRooms():
    access_token = os.getenv("ACCESSTOKEN")
    apiUrl = "https://api.ciscospark.com/v1/rooms"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    response = requests.get(url=apiUrl, headers=httpHeaders)
    data=json.loads(response.text)
    i=1

    for id in data['items']:
        if str(os.getenv("CLASSPREFIX")) in str(id['title']):
            apiUrl = "https://api.ciscospark.com/v1/rooms/"+str(id['id'])
            httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
            response = requests.delete(url=apiUrl, headers=httpHeaders)
            if (response.status_code==204):
                print ('Raum ' + str(i) + ' : '+ str(id['title']) + ' gelöscht')

            i+=1

def deleteWebhooks():
    access_token = os.getenv("ACCESSTOKEN")
    apiUrl = "https://api.ciscospark.com/v1/webhooks"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    response = requests.get(url=apiUrl, headers=httpHeaders)
    data=json.loads(response.text)
    i=1

    for id in data['items']:
        if str(os.getenv("CLASSPREFIX")) in str(id['name']):
            apiUrl = "https://api.ciscospark.com/v1/webhooks/"+str(id['id'])
            httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
            response = requests.delete(url=apiUrl, headers=httpHeaders)
            if (response.status_code==204):
                print ('Webhook ' + str(i) + ' : '+ str(id['name']) + ' gelöscht')

            i+=1

def listWebhooks():
    access_token = os.getenv("ACCESSTOKEN")
    apiUrl = "https://api.ciscospark.com/v1/webhooks"
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    response = requests.get(url=apiUrl, headers=httpHeaders)
    data=json.loads(response.text)
    i=1

    for id in data['items']:
        if str(os.getenv("CLASSPREFIX")) in str(id['name']):
            print ('Webhook ' + str(i) + ' : '+ str(id['name']))
            i+=1

    

def main():
    i=0

    while i==0:
        Eingabe=int(input('\nInitialisieren der Laborumgebung 1\nListe der fraglichen Webhooks 2\nLöschen der Webhooks 3\nListe der Räume 4\nLöschen der Räume 5\nAlles löschen 6\n-> '))
        if (Eingabe==1):
            print (str(initLab.initLab()))
        if (Eingabe==2):
            listWebhooks()
        if (Eingabe==3):
            deleteWebhooks()
        if (Eingabe==4):
            listRooms()
        if (Eingabe==5):
            deleteRooms()
        if (Eingabe==6):
            deleteRooms()
            deleteWebhooks()
        

main()
