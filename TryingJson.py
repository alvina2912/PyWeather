
import json

import easygui


def Mbox(msg):
     easygui.msgbox(msg, title="Weather Condition", ok_button="OK")

data=open('sample.json')
js = json.load(data)


print json.dumps(js,indent=4)
id_=js['weather'][0]['id']
mainWeather=js['weather'][0]['main']
description=js['weather'][0]['description']
temp=js['main']['temp']
print "ID : ",id_
print "Main Weather : ", mainWeather
print "Deacription : ",description
print "Temprature : ",temp
msg=mainWeather+"--"+description

if (id_==800 or id_==200 or id_==201 or id_==202 or id_==211 or id_==212
   or id_==221 or id_==231 or id_==231 or id_==232 or id_==312 or id_==314
   or id_==502 or id_==503 or id_==504 or id_==511 or id_==522 or id_== 602
   or id_==622 or id_==701 or id_==711 or id_==721 or id_==731 or id_==741
   or id_==751 or id_==761 or id_==771 or id_==781 or id_==900 or id_==901
   or id_==902 or id_==903 or id_==904 or id_==905 or id_==906 or id_==960
   or id_==961 or id_==962):
   Mbox(msg)
