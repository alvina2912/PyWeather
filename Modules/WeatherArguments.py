def parsingArguments(arguments):

    argumentsDict={'mode':'EMAIL',
            'timeInterval':1,
            'sender' : 'abc@gmail.com',
            'password':'123abc',
            'receiver':'abc',
            'location':'MapleGrove,USA',
            'apiid':'12ab',
            'weatherChoice':'normal'
            }
    for i in arguments[1:]:
        k,v=i.split(":")
        if k in argumentsDict.keys():
            argumentsDict[k]=v
    return argumentsDict
