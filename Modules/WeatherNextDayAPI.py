import urllib
import json
import WeatherConfig
import datetime

today = datetime.date.today()
tomorrow= today+ datetime.timedelta(days=1)


dt_txt=str(tomorrow)+" 09:00:00"

def getNextDayWeatherInfo(nextDayURL):
    uh = urllib.urlopen(nextDayURL)
    data = uh.read()

    try: js = json.loads(str(data))
    except: js = None

    for i in range (len(js['list'])):
        if dt_txt==js['list'][i]['dt_txt']:

            nextDayTemp=js['list'][i]['main']['temp']
            nextDayWeather=js['list'][i]['weather'][0]['main']
            nextDayDescription=js['list'][i]['weather'][0]['description']

    nextDayTemp=1.8 * (nextDayTemp - 273) + 32
    nextDayDescription=nextDayDescription.title()
    #print nextDayDescription
    #print nextDayTemp
    return nextDayDescription,nextDayTemp
