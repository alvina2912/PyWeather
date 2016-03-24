import urllib
import json
import WeatherConfig

'''NormalWeatherCodes=[210,300,301,302,310,311,313,321,501,520,521,531,600,601,611,612,615,616,620,621,721,
    800,801,802,803,804,951,952,953,954,955,956,957,958,959]
BadWeatherCodes = [200,201,202,211,212,221,230,231,232,312,314,502,503,504,511,522,602,
   622 ,701 ,711 ,731,741,751 ,761,771,781,900,901,902,903,904,905 ,906 ,960,961, 962]'''

def getInfo(url):

    uh = urllib.urlopen(url)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None

    id_=js['weather'][0]['id']
    mainWeather=js['weather'][0]['main']
    description=js['weather'][0]['description']
    temp=js['main']['temp']
    mainTemp=1.8 * (temp - 273) + 32
    print "ID : ",id_
    print "Main Weather : ", mainWeather
    print "Deacription : ",description
    print "Temprature : ",mainTemp
    description=description.title()
    mainTemp=str(mainTemp)
    return (id_ ,description,mainTemp)
