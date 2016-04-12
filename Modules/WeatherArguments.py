def parseArguments(arguments):

    argumentsDict={'mode':'EMAIL',
            'timeInterval':1,
            'sender' : None,
            'password':None,
            'receiver':None,
            'location':None,
            'apiid': None,
            'weatherChoice':'normal'
            }
    for i in arguments[1:]:
        k,v=i.split(":")
        if k in argumentsDict.keys():
            argumentsDict[k]=v
    argumentsDict = validateArguments(argumentsDict)
    return argumentsDict


def validateArguments(argumentsDict):
    if argumentsDict['apiid']==None:
        print "apiid is missing"
        return None
    elif argumentsDict['mode']=='EMAIL':
        if argumentsDict['sender']==None:
            print "sender is missing"
            return None
        elif argumentsDict['password']==None:
            print "password is missing"
            return None
        elif argumentsDict['receiver']==None:
            print "receiver is missing"
            return None
    elif argumentsDict['location']==None:
        print "location is missing"
        return None

    return argumentsDict
