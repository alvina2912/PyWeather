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
url=WeatherConfig.setLocation(location)
id_ , description , mainTemp = WeatherAPI.getInfo(url)




def getMsg():
    timeInterval=int(mydict['timeInterval'])
    timeInterval = timeInterval * 60
    if description is not  None:
        imgName=WeatherIcon.getImg(id_)
        WeatherUI.Mbox(imgName,description,mainTemp)
        time.sleep(timeInterval)

def getEmail():
    if description is not  None:
        WeatherEmailNotification.sendEmail(description,mainTemp,sender,receiver,password)


if mode=='UI':
    while True:
        getMsg()
elif mode=="EMAIL":
    getEmail()
