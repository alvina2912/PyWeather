def setLocation(location):
    url = 'http://api.openweathermap.org/data/2.5/weather?q='+location+'%20USA&appid=698e799746db6c7d7958b1bbd6582cc3'
    return url

codes={
200 :"Storm.gif",201 :"Storm.gif",202 :"Storm.gif",211 :"Storm.gif",212 :"Storm.gif",
221 :"Storm.gif",230 :"Storm.gif",231 :"Storm.gif",232 :"Storm.gif",210 :"Storm.gif",
960 :"Storm.gif",901 :"Storm.gif",961 :"Storm.gif",701 :"Mist1.gif",300 :"Raining.gif",
301 :"Raining.gif",302 :"Raining.gif",310 :"Raining.gif",311 :"Raining.gif",
313 :"Raining.gif",321 :"Raining.gif",312 :"Raining.gif",314 :"Raining.gif",
501 :"Raining.gif",520 :"Raining.gif",521 :"Raining.gif",531 :"Raining.gif",
502 :"Raining.gif",503 :"Raining.gif",504 :"Raining.gif",511 :"Raining.gif",
522 :"Raining.gif",600 :"Snow.gif",601 :"Snow.gif",611 :"Snow.gif",612 :"Snow.gif",
615 :"Snow.gif",616 :"Snow.gif",620 :"Snow.gif",621 :"Snow.gif",602 :"Snow.gif",
622 :"Snow.gif",801 :"Cloudy.gif",802 :"Cloudy.gif",803 :"Cloudy.gif",
804 :"Cloudy.gif",781 :"tornado.gif",900 :"tornado.gif",902 :"hurricane.gif",
962 :"hurricane.gif",905 :"wind.gif",800 :"Sunny.gif"
}

NormalWeatherCodes={
210:"Storm.gif",300:"Raining.gif",301:"Raining.gif",302:"Raining.gif",310:"Raining.gif",
311:"Raining.gif",313:"Raining.gif",321:"Raining.gif",501:"Raining.gif",520:"Raining.gif",
521:"Raining.gif",531:"Raining.gif",600:"Snow.gif",601:"Snow.gif",611:"Snow.gif",
612:"Snow.gif",615:"Snow.gif",616:"Snow.gif",620:"Snow.gif",621:"Snow.gif",721,
    800:"Sunny.gif",801:"Cloudy.gif",802:"Cloudy.gif",803:"Cloudy.gif",804:"Cloudy.gif",
    951,952,953,954,955,956,957,958,959
    }

BadWeatherCodes = {
200:"Storm.gif",201:"Storm.gif",202:"Storm.gif",211:"Storm.gif",212:"Storm.gif",
221:"Storm.gif",230:"Storm.gif",231:"Storm.gif",232:"Storm.gif",312:"Raining.gif",
314:"Raining.gif",502:"Raining.gif",503:"Raining.gif",504:"Raining.gif",511:"Raining.gif",
522:"Raining.gif",602,
622:"Snow.gif" ,701:"Mist1.gif" ,711 ,731:"dust.gif",741,751 ,761,771,781:"tornado.gif",
900:"tornado.gif",901:"Storm.gif",902:"hurricane.gif",903:"cold.gif",904:"hot.gif",905:"wind.gif" ,906:"Hail.gif",
960:"Storm.gif",
961:"Storm.gif", 962:"hurricane.gif"
   }
