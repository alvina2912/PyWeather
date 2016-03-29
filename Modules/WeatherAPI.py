import urllib
import json
import WeatherConfig


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
