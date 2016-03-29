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
mydict={}

mydict= WeatherArguments.parsingArguments(arguments)
mode=mydict['mode']
sender=mydict['sender']
receiver=mydict['receiver']
password=mydict['password']
location=mydict['location']
city,country=location.split(",")
timeInterval=int(mydict['timeInterval'])
apiid=mydict['apiid']
timeInterval = timeInterval * 60
print mode,sender,receiver,password,location
url=WeatherConfig.url.format(city,country,apiid)
id_ , description , mainTemp = WeatherAPI.getInfo(url)


def getMsg():
    if description is not  None:
        if mode=="UI":
            imgName=WeatherIcon.getImg(id_)
            WeatherUI.Mbox(imgName,description,mainTemp)
            time.sleep(timeInterval)
        elif mode=="EMAIL":
            WeatherEmailNotification.sendEmail(description,mainTemp,sender,receiver,password)
            time.sleep(timeInterval)

while True:
        getMsg()
