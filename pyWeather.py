import sys
sys.path.append('/Users/rogerpereira/Documents/Projects/PyWeather/Moduls')

import time
import WeatherAPI
import WeatherUI
import WeatherIcon

id_ ,msg = WeatherAPI.getInfo()
def getMsg():
    if msg is not  None:
        imgName=WeatherIcon.getImg(id_)
        WeatherUI.Mbox(imgName,msg)
        time.sleep(60)

while True:
    getMsg()
