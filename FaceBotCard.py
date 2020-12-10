# Dieses File dient nur zur Demonstration von Webhooks. Für diese Anwendung wurden zwei Webhooks eingerichtet. Einer feuert bei Erstellung einer Nachricht,
# Ein weiterer feuert bei Erstellen eines Attachments. Die Zahlen in den Kommentaren, sollen Ihnen einen Hinweis auf die Auswertungsreihenfolge geben.

# wir importieren flask als simple Möglichkeit einen Webeserver zu betreiben
from flask import Flask, request
import json
import re
import os
import requests
import FaceRecognizer
import FunctionPostMessageToRoom

access_token = os.getenv("ACCESSTOKEN")
email='none'
name='none'

# Die Adaptive Card habe ich zur Übersichtlichkeit in die Datei SampleAdaptiveCard.json gespeichert. Diese wird hier geladen, und in der Variable sampleAdaptiveCard hinterlegt
with open('SampleAdaptiveCard.json','r') as json_file:
    #print (type(json_file))
    sampleAdaptiveCard = json.load(json_file)
    #print (type(sampleAdaptiveCard))
    #print (sampleAdaptiveCard)

# Flask wird als Variable "app" referenziert
app = Flask(__name__)

def generateText(Age,Gender,Smile):
    Gechlecht=None
    Laecheln=str(Smile*100)
    Age=str(Age)
    if Gender=='male':
        print ('MÄNNLICH')
        Geschlecht='männlich'
    if Gender=='female':
        print ('WEIBLICH')
        Geschlecht='weiblich'
    text="Die Person auf dem Bild schätze ich auf "+Age+" Lebensjahre. Ausserdem bin ich mir sicher, dass die Person "+Geschlecht+" ist. Die Person zeigt ein "+Laecheln+" prozentiges Lächeln."
    return text



def sendpicture(avatarurl,name):
    data = FaceRecognizer.recognize_face(avatarurl)
    attrAge=data[0]['faceAttributes']['age']
    attrGender=data[0]['faceAttributes']['gender']
    attrSmile=data[0]['faceAttributes']['smile']
    text=generateText(attrAge,attrGender,attrSmile)
    print(json.dumps(data, indent=4, sort_keys=True))
    message = str(json.dumps(data, indent=4, sort_keys=True))
    #FunctionPostMessageToRoom.sendtext(str(json.dumps(data, indent=4, sort_keys=True)))
    #print (avatarurl)
    cardstring='{"contentType":"application/vnd.microsoft.card.adaptive","content":{"$schema":"http://adaptivecards.io/schemas/adaptive-card.json","type":"AdaptiveCard","version":"1.0","body":[{"type":"TextBlock","size":"Medium","weight":"Bolder","text":"Ergebnis der Analyse","horizontalAlignment":"Center"},{"type":"ColumnSet","columns":[{"type":"Column","width":"auto","items":[{"type":"Image","style":"Person","url":"'+avatarurl+'","size":"Large"}]},{"type":"Column","width":"stretch","items":[{"type":"TextBlock","weight":"Bolder","text":"'+name+'","wrap":true},{"type":"TextBlock","text":"'+text+'","wrap":true}]}]}]}}'

    cardjson=json.loads(cardstring)
    
    apiUrl = "https://api.ciscospark.com/v1/messages"
    body = {"roomId" : os.getenv("ROOMID"),"markdown":"This is an adaptive Card", "attachments" : cardjson}
    #print('**********************************************************************************************************************************')
    #print(json.dumps(body, indent=4, sort_keys=False))
    #print('**********************************************************************************************************************************')
    
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    # Das Ergebnis der Rückgabe wird in Request gespeichert.
    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)
    print(response.text)



def getAvatarURL(email):
    print('Suche das Avatarbild für : '+email)
    apiUrl = "https://api.ciscospark.com/v1/people?email="+email
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body={}
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    data=json.loads(response.text)
    print(json.dumps(data, indent=4, sort_keys=True))
    print ("Die AvatarURL lautet: "+str(data['items'][0]['avatar']))
    avatarurl=data['items'][0]['avatar']
    name=data['items'][0]['displayName']
    sendpicture(avatarurl,name)
    

def getAttachment(attachmentID):
    # 6. Wurde in 2. der Anhangstyp "AttachmentActions" erkannt, landen wir hier
    print ("Ich hole den Anhang mit ID: "+attachmentID)
    apiUrl = "https://api.ciscospark.com/v1/attachment/actions/"+attachmentID
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body={}
    # Wor laden das Attachment
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    data=json.loads(response.text)
    # Die Ausgabe erfolgt nachfolgend ein wenig geschönt:
    #print(json.dumps(data, indent=4, sort_keys=True))
    # Oder hier eine formatierte Variante:
    email=str(data['inputs']['Email'])
    print ("Die Emailadresse lautet: " + str(data['inputs']['Email']))
    print ("Der eingegebene Name: " + str(data['inputs']['Name']))
    print ("Die genannte Telefonnummer: " + str(data['inputs']['Tel']))
    print ("Das GitHub Repository: " + str(data['inputs']['Url']))
    getAvatarURL (email)

        

# 5. Nun senden wir die Karte an den übergebenen Raum
def sendCard(roomId):
    print ('sendCard wurde gerufen in Raum: '+roomId)
    # Wie gehabt werden ersteinmal die Aufruf URL, der Body, sowie der Header erstellt.
    apiUrl = "https://api.ciscospark.com/v1/messages"
    body = {"roomId" : roomId,"markdown":"This is an adaptive Card", "attachments" : sampleAdaptiveCard}
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    # Das Ergebnis der Rückgabe wird in Request gespeichert.
    response = requests.post(url=apiUrl, json=body, headers=httpHeaders)
    #print(response.text)
    #Herausforderung - Geben Sie eine Zeile aus, wenn die Rückgabe bestätigt, daß die Karte erfolgreich verschickt wurde.

# 4. Wir holen die Nachricht ab  
def getMessage(messageID):
    # Dazu erstellen wir zunächst die Standardkomponenten Header und Body, sowie die AufrufURL
    # Wir hängen die MessageID aus der Übergabe des Funktionsaufrufs an.
    apiUrl = "https://api.ciscospark.com/v1/messages/"+messageID
    access_token = os.getenv("ACCESSTOKEN")
    httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
    body = {}
    # Wir speichern das Ergebnis des Aufrufs in die Variable response
    response = requests.get(url=apiUrl, json=body, headers=httpHeaders)
    # und überführen den Textteil in eine dictionary Variable "data"
    data=json.loads(response.text)
    print (data)
    if (data['text']):
        print (data['personEmail'] + ' schrieb: ' + data['text'])
        roomId=data['roomId']
        # Dann werten wir den Text aus
        # Wir reagieren nur, wenn der Inhalt des Texts "card" lautet
    
        if str(data['text']) == 'card':
            print ('Ich habe "card" gehört... ich sollte reagieren')
            # Danach rufen wir die Funktion sendCard(roomId) und übergeben die roomId
            sendCard(roomId)



 
# 2. Die Flask Methoden werden spezifiziert- Wir erlauben POST und GET Methoden, wobei die GET Methode keinen Einfluss auf unsere Funktion nimmt
@app.route('/', methods=['POST','GET'])
def index():
    if request.method=='GET':
        return ('Webserver für simple Webhooks', 200, None)
    
    # 3. Empfangen wir ein POST Request, müssen wir zunächst untersuchen, ob wir eine auswertbare Nachricht, oder ein Attachment geschickt bekamen.
    # Daher sehen wir uns den JSON Block genauer an.
    if request.method=='POST':
        # Wir lesen den Datenteil in ein JSON Dict "data"  
        data = json.loads(request.data)
        print(data)
        # print (data['data']['id'])
        # Wenn wir im Schlüsselelemt 'resource' den Wert 'messages' entdecken
        if data['resource']=="messages":
            messageID=data['data']['id']
            # Dann werten wir die Nachricht über die Funktion getMessage(messageId) aus. 
            getMessage(messageID)
        
        # Wenn wir im Schlüsselelemt 'resource' den Wert 'attachmentActions' entdecken...
        if data['resource']=="attachmentActions":
            print('Anhang gefunden')
            print("Die Anhang ID ist: "+ str(data['data']['id']))
            # ... holen wir das Attachment mit der Funktion getAttachment () und übergeben die id der Daten
            getAttachment(str(data['data']['id']))
        return '{"success":"true"}'        

# 1. Flask wird gestartet
if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

