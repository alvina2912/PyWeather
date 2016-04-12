
# PyWeather
A simple utility application to retrieve and notify current weather information via email or UI message box periodically. The application can be run as a daemon on mac or as a windows service on windows PC.
## Author
Alvina Pereira
## Prerequisites
[Python 2.7.11](https://www.python.org/downloads)
## Example
```
$ python pyWeather.py apiid:<apiid> weatherChoice:severe timeInterval:60 location:MapleGrove,USA mode:EMAIL sender:abc@gmail.com password:abc123 receiver:abc@gmail.com,xyz@gmail.com
```

The above command will run pyWeather with EMAIL mode and will retrieve weather information every 60 minutes notifying receivers about severe weather via email.

## About the app

1. The app uses [Open Weather Map API](https://home.openweathermap.org) to retrieve weather information.
2. An API KEY is needed to be passed as command line argument as shown above for the app to run. The api key can be obtained by creating a free account on [Open Weather Map API](https://home.openweathermap.org)
3. For the UI mode, the app uses cross-platform UI module [easygui](http://easygui.sourceforge.net/)
4. For the EMAIL mode, the app supports GMAIL as of now but can be easily extended to support other email providers.
5. Following is the list of available command line arguments. Arguments with * are mandatory arguments.
      * __apiid*__ : A valid API key for weather api  
      * __location*__ :city name comma country
      * __mode__ : EMAIL or UI. Default _EMAIL_
      * __timeIntervel__ : A time interval number in minutes. Default _60_  
      * __sender__: Sender's email address. For _EMAIL_ mode than this argument is mandatory.
      * __password__ : Sender's password. For _EMAIL_ mode this argument is mandatory.
      * __receiver__: Email notification receiver's email addresses separated by comma. For _EMAIL_ mode this argument is mandatory.
      * __weatherChoice__ : normal or severe. Default _normal_  


## Final Word

PyWeather is developed as a small project for fun & learning python and is no way intended to be used for any business / commercial use.
