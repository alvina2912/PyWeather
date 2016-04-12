import smtplib,string
import time

currentTime=  (time.strftime("%I:%M:%S"))

def sendEmail(description,mainTemp,sender,receiver,password):
    Subj = "Weather condition at "+currentTime
    text="Todays Weather : "+description
    temp="Temprature : "+mainTemp+"F"
    Text = """ %s \n %s """ %(text,temp)
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
