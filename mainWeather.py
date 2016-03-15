import time
import WeatherAPI
import UI
import getIcon

id_ ,msg = WeatherAPI.getInfo()
def getMsg():
    if msg is not  None:
        imgName=getIcon.getImg(id_)
        UI.Mbox(imgName,msg)
        time.sleep(60*2)

while True:
    getMsg()
