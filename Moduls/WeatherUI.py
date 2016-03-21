import easygui
import WeatherIcon

def Mbox(imgName,msg):
    #200 - ../Images/storm.gif
     image = "Images//"+imgName
     easygui.msgbox(msg, image=image,ok_button="OK" )
