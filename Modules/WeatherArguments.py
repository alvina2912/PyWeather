def parsingArguments(arguments):

    mydict={'mode':'UI',
            'timeInterval':1,
            'sender' : 'abc@gmail.com',
            'password':'123abc',
            'receiver':'abc',
            'location':'MapleGrove'
            }
    for i in arguments[1:]:
        k,v=i.split(":")
        if k=='mode':
            mydict[k]=v
        elif k=='timeInterval':
            mydict[k]=v
        elif k=='sender':
            mydict[k]=v
        elif k=='password':
            mydict[k]=v
        elif k=='receiver':
            mydict[k]=v
        elif k=='location':
            mydict[k]=v
    return mydict
