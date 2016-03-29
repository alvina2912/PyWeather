def parsingArguments(arguments):

    mydict={'mode':'EMAIL',
            'timeInterval':1,
            'sender' : 'abc@gmail.com',
            'password':'123abc',
            'receiver':'abc',
            'location':'MapleGrove,USA',
            'apiid':'12ab'
            }
    for i in arguments[1:]:
        k,v=i.split(":")
        if k in mydict.keys():
            mydict[k]=v
    return mydict
