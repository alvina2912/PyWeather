import smtplib,string

def sendEmail(description,mainTemp,sender,receiver,password):
    Subj = "Weather condition"
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
    smtpobj.sendmail(sender,receiver,Body )
    print "Susscesfully email send"
    smtpobj.close()
