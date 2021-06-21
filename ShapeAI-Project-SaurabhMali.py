import requests, json
from datetime import datetime

api_key = 'ae10058fc8082939aa649a9005db19ad'
location = input("Enter City Name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()


#create variables to store and display data
tempc_city = (api_data['main']['temp'])
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature(FAHRENHEIT) : {:.2f} °F  ".format(tempc_city))
print ("Current temperature(CELSIUS) : {:.2f} °C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Humidity      :",hmdt, '%')
print ("Current wind speed    :",wind_spd ,'kmph')


with open('detail.txt', 'wb') as fd: 
    fd.write(api_link.content)

