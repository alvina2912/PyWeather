import sys
sys.path.append('Modules')

import time
import WeatherAPI
import WeatherUI
import WeatherIcon
import WeatherEmailNotification
import WeatherArguments
import WeatherConfig
import WeatherNextDayAPI


arguments=sys.argv
argumentsDict={}

argumentsDict= WeatherArguments.parseArguments(arguments)
#print argumentsDict
if argumentsDict==None:
    sys.exit()
else:
    mode=argumentsDict['mode']
    sender=argumentsDict['sender']
    receiver=argumentsDict['receiver']
    password=argumentsDict['password']
    location=argumentsDict['location']
    timeInterval=int(argumentsDict['timeInterval'])
    apiid=argumentsDict['apiid']
    weatherCondition=argumentsDict['weatherChoice']
timeInterval = timeInterval * 60
city,country=location.split(",")
url=WeatherConfig.url.format(city,country,apiid)
nextDayURL=WeatherConfig.nextDayURL.format(city,country,apiid)



def weatherNotification():
    id_ , description , mainTemp = WeatherAPI.getInfo(url)
    nextDayDescription,nextDayTemp=WeatherNextDayAPI.getNextDayWeatherInfo(nextDayURL)

    isSevereWeather = False
    if weatherCondition=="severe" :
        if id_ in WeatherConfig.BadWeatherCodes.keys():
            isSevereWeather = True
    if description is not  None:
        if mode=="UI":
            imgName=WeatherIcon.getImg(id_)
            if weatherCondition == "severe" and isSevereWeather == True:
                WeatherUI.Mbox(imgName,description,mainTemp,nextDayDescription,nextDayTemp)
            elif weatherCondition == "normal":
                WeatherUI.Mbox(imgName,description,mainTemp,nextDayDescription,nextDayTemp)
        elif mode=="EMAIL":
            if weatherCondition == "severe" and isSevereWeather == True:
                WeatherEmailNotification.sendEmail(description,mainTemp,nextDayDescription,nextDayTemp,sender,receiver,password)
            elif weatherCondition == "normal":
                WeatherEmailNotification.sendEmail(description,mainTemp,nextDayDescription,nextDayTemp,sender,receiver,password)
        time.sleep(timeInterval)

while True:
        weatherNotification()
