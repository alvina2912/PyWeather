import WeatherAPI

def getImg(id_):
    id_=id_
    imgName=""
    if id_ in [200,201,202,211,212,221,230,231,232,210]:
        imgName="Storm"
    elif id_ == 701 :
        imgName="Mist1"
    elif id_ in [300,301,302,310,311,313,321,312,314,501,520,521,531,502,503,504,511,522]:
        imgName="Raining"
    elif id_ in [600,601,611,612,615,616,620,621,602,622]:
        imgName="Snow"
    elif id_ in [801,802,803,804 ]:
        imgName="Cloudy"
    elif id_ ==800 :
        imgName="Sunny"
    return imgName
