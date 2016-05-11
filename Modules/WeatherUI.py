import easygui
import WeatherIcon
import WeatherNextDayUI
import time

currentTime=  (time.strftime("%I:%M:%S"))
def Mbox(imgName,description,mainTemp,nextDayDescription,nextDayTemp):
     nextDayWeatherInfo=WeatherNextDayUI.getNextDayWeather(nextDayDescription,nextDayTemp)
     image = "Images//"+imgName
     msg="Today's Weather at "+currentTime+"  "+description+"\n Temprature : "+mainTemp+"F\n"+nextDayWeatherInfo
     easygui.msgbox(msg, image=image,ok_button="OK" )
