import smtplib,string
import time

currentTime=  (time.strftime("%I:%M:%S"))

def sendEmail(description,mainTemp,nextDayDescription,nextDayTemp,sender,receiver,password):
    Subj = "Weather condition at "+currentTime
    text="Today's Weather : "+description
    temp="Temprature : "+mainTemp+"F"
    nexDayText="Tomorrow's Weather at 09:00 am : "+nextDayDescription
    nextDaytemp="Temprature : "+str(nextDayTemp)+"F"
    Text = """ %s \n %s \n %s \n %s """ %(text,temp,nexDayText,nextDaytemp)
    Body = string.join((
        "From: %s" % sender,
        "To: %s" % receiver,
        "Subject: %s" % Subj,
        "",
        Text,
        ), "\r\n")

    smtpobj=smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    smtpobj.login(sender,password)
    smtpobj.sendmail(sender,receiver.split(","),Body )

    smtpobj.close()
