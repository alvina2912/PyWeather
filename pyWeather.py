import sys
sys.path.append('Modules')

import time
import WeatherAPI
import WeatherUI
import WeatherIcon
import WeatherEmailNotification
import WeatherArguments
import WeatherConfig


arguments=sys.argv
argumentsDict={}

argumentsDict= WeatherArguments.parsingArguments(arguments)
mode=argumentsDict['mode']
sender=argumentsDict['sender']
receiver=argumentsDict['receiver']
password=argumentsDict['password']
location=argumentsDict['location']
city,country=location.split(",")
timeInterval=int(argumentsDict['timeInterval'])
apiid=argumentsDict['apiid']
weatherCondition=argumentsDict['weatherChoice']
timeInterval = timeInterval * 60
url=WeatherConfig.url.format(city,country,apiid)


def weatherNotification():
    id_ , description , mainTemp = WeatherAPI.getInfo(url)
    isSevereWeather = False
    if weatherCondition=="severe" :
        if id_ in WeatherConfig.BadWeatherCodes.keys():
            isSevereWeather = True
    if description is not  None:
        if mode=="UI":
            imgName=WeatherIcon.getImg(id_)
            if weatherCondition == "severe" and isSevereWeather == True:
                WeatherUI.Mbox(imgName,description,mainTemp)
            elif weatherCondition == "normal":
                WeatherUI.Mbox(imgName,description,mainTemp)
        elif mode=="EMAIL":
            if weatherCondition == "severe" and isSevereWeather == True:
                WeatherEmailNotification.sendEmail(description,mainTemp,sender,receiver,password)
            elif weatherCondition == "normal":
                WeatherEmailNotification.sendEmail(description,mainTemp,sender,receiver,password)
        time.sleep(timeInterval)

while True:
        weatherNotification()
