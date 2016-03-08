import urllib
import json
import ctypes
import easygui


def Mbox(title, text):
     easygui.msgbox(0, text, title)

serviceurl = 'http://api.openweathermap.org/data/2.5/weather?q=MapleGrove%20USA&appid=44db6a862fba0b067b1930da0d769e98'

uh = urllib.urlopen(serviceurl)
data = uh.read()
#print 'Retrieved',len(data),'characters'

try: js = json.loads(str(data))
except: js = None

print json.dumps(js,indent=4)
id=js['weather'][0]['id']
mainWeather=js['weather'][0]['main']
description=js['weather'][0]['description']
temp=js['main']['temp']
print "ID : ",id
print "Main Weather : ", mainWeather
print "Deacription : ",description
print "Temprature : ",temp

if id==803:
    Mbox(mainWeather,description )
