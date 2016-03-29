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
timeInterval = timeInterval * 60
url=WeatherConfig.url.format(city,country,apiid)
id_ , description , mainTemp = WeatherAPI.getInfo(url)



def weatherNotification():
    if description is not  None:
        if mode=="UI":
            imgName=WeatherIcon.getImg(id_)
            WeatherUI.Mbox(imgName,description,mainTemp)
        elif mode=="EMAIL":
            WeatherEmailNotification.sendEmail(description,mainTemp,sender,receiver,password)
        time.sleep(timeInterval)
while True:
        weatherNotification()
