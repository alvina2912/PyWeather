import smtplib

def sendEmail(description,mainTemp,sender,receiver,password):
    msg = ("From: %s\r\nTo: %s \r\n\r\n" % (sender, receiver))
    text="Todays Weather : "+description
    temp="Temprature : "+mainTemp
    msg=msg+text+"\n"+temp
    smtpobj=smtplib.SMTP_SSL('smtp.googlemail.com', 465)
    smtpobj.login(sender,password)
    smtpobj.sendmail(sender,receiver,msg )
    print "Susscesfully email send"
    smtpobj.close()
