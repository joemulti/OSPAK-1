import initCreateRoom
import initCreateWebhook
import initCreateWebhookForAdaptiveCards
import re
import datetime

calendarweek=(datetime.date.today().isocalendar()[1])
classprefix='KW'+str(calendarweek)

regexroom = re.compile('ROOMID = ".*"')
regexwebhook = re.compile('WEBHOOKID = ".*"')
regexattwebhook = re.compile('WEBHOOKATT = ".*"')
regexclassprefix = re.compile('CLASSPREFIX = ".*"')
regexwebhookname = re.compile('WEBHOOKNAME = ".*"')
regexwebhookattname = re.compile('WEBHOOKATTNAME = ".*"')

def initLab():
    classroomid,classroomtitle=initCreateRoom.createRoom(classprefix)
    print ('Space mit dem Titel : '+classroomtitle+' wurde angelegt')
    classroomwebhookid,classroomwebhookname=initCreateWebhook.createWebhook(classroomid)
    print ('Webhook mit dem Titel : '+classroomwebhookname+' wurde angelegt')
    classroomattwebhookid,classroomattwebhookname=initCreateWebhookForAdaptiveCards.createAttWebhook(classroomid)
    print ('Webhook mit dem Titel : '+classroomattwebhookname+' wurde angelegt')


    def changeenv():
        with open(".env") as fobj_in:
            environmentvariablelist=[]
            for line in fobj_in.readlines():
                line=re.sub(regexroom,'ROOMID = "'+classroomid+'"',line)
                line=re.sub(regexwebhook,'WEBHOOKID = "'+classroomwebhookid+'"',line)
                line=re.sub(regexattwebhook,'WEBHOOKATT = "'+classroomattwebhookid+'"',line)
                line=re.sub(regexclassprefix,'CLASSPREFIX = "'+classprefix+'"',line)
                line=re.sub(regexwebhookname,'WEBHOOKNAME = "'+classroomwebhookname+'"',line)
                line=re.sub(regexwebhookattname,'WEBHOOKATTNAME = "'+classroomattwebhookname+'"',line)
                environmentvariablelist.append(line)

        with open('.env', 'w') as fobj_out:
            for line in environmentvariablelist:
                fobj_out.write("%s" % line)
        print ('Environment angepasst')

    changeenv()
    return ('Die Laborumgebung wurde eingerichtet')