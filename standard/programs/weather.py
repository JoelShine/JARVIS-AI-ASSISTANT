import requests
import json
import sys
import math

# for removing extra weather digits
def truncate(number, digits) -> float:
    stepper = 10.0 ** digits
    return math.trunc(stepper * number) / stepper

api_key = "69bf0a590576448ed0bfd804ac2b2694"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
n = len(sys.argv)

city_name = 

complete_url = base_url + "appid=" + api_key + "&q=" + city_name

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    current_humidiy = y["humidity"]

    z = x["weather"]
    weather_description = z[0]["description"]
    celsius = current_temperature-273.15

    speak("Sir, Temperature in " + city_name +"is" + str(truncate(celsius, 2)) + " degree celsius")

    print("Temperature in Celsius = " + str(truncate(celsius, 2)) + " degree celsius")
    print("Temperature in Farenheit = " + str(truncate(celsius*9/5+32, 2)) + " degree farenheit")

    speak("The weather description is " + str(weather_description))

    print("Atmospheric pressure = " + str(current_pressure) + " mb")
    print("Humidity = " + str(current_humidiy) + " %")
    print("Description = " + str(weather_description))
    print("")

else:
    print(" City Not Found. Please try again.")
