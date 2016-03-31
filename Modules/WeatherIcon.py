import WeatherAPI
import WeatherConfig

def getImg(id_):
    imgName=""
    if id_ in WeatherConfig.codes:
        imgName=WeatherConfig.codes[id_]
    return imgName
