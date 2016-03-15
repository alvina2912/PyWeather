import urllib
import json

NormalWeatherCodes=[210,300,301,302,310,311,313,321,501,520,521,531,600,601,611,612,615,616,620,621,721,
    800,801,802,803,804,951,952,953,954,955,956,957,958,959]
BadWeatherCodes = [200,201,202,211,212,221,230,231,232,312,314,502,503,504,511,522,602,
   622 ,701 ,711 ,731,741,751 ,761,771,781,900,901,902,903,904,905 ,906 ,960,961, 962]

def getInfo():
    serviceurl = 'http://api.openweathermap.org/data/2.5/weather?q=MapleGrove%20USA&appid=698e799746db6c7d7958b1bbd6582cc3'

    uh = urllib.urlopen(serviceurl)
    data = uh.read()
    #data=open('sample.json')

    try: js = json.loads(str(data))
    except: js = None

    #print json.dumps(js,indent=4)
    id_=js['weather'][0]['id']
    mainWeather=js['weather'][0]['main']
    description=js['weather'][0]['description']
    temp=js['main']['temp']
    mainTemp=1.8 * (temp - 273) + 32
    print "ID : ",id_
    print "Main Weather : ", mainWeather
    print "Deacription : ",description
    print "Temprature : ",mainTemp
    msg="Today's Weather :"+mainWeather+"\n Temprature : "+str(mainTemp)+"F"
    #if id_ in BadWeatherCodes or id_ in NormalWeatherCodes:
    return (id_ ,msg)


def getInfoMock():
    return 800, "Great Weather"
