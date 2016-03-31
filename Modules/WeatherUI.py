import easygui
import WeatherIcon
import time

currentTime=  (time.strftime("%I:%M:%S"))
def Mbox(imgName,description,mainTemp):

     image = "Images//"+imgName
     msg="Today's Weather at "+currentTime+"  "+description+"\n Temprature : "+mainTemp+"F"
     easygui.msgbox(msg, image=image,ok_button="OK" )
