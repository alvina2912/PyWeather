import easygui
import WeatherIcon

def Mbox(imgName,description,mainTemp):

     image = "Images//"+imgName
     msg="Today's Weather :"+description+"\n Temprature : "+mainTemp+"F"
     easygui.msgbox(msg, image=image,ok_button="OK" )
