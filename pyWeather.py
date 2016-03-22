import sys
sys.path.append('Modules')

import time
import WeatherAPI
import WeatherUI
import WeatherIcon

id_ ,msg = WeatherAPI.getInfo()
arguments=sys.argv
t = 1
if len(arguments) > 1:
    t=int(arguments[1])
t = t * 60
def getMsg():
    if msg is not  None:
        imgName=WeatherIcon.getImg(id_)
        WeatherUI.Mbox(imgName,msg)
        time.sleep(t)

while(True):
    getMsg()
