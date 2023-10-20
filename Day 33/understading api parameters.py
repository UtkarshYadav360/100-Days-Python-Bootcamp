import requests
import datetime as dt

# CONSTANTS
MY_LATITUDE = 28.669155
MY_LONGITUDE = 77.453758

# understanding API parameters :
parameters = {"lat": MY_LATITUDE, "lng": MY_LONGITUDE, "formatted": 0}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
# print(data)

sunrise = data["results"]["sunrise"]
print(sunrise)
print(sunrise.split("T"))
print(sunrise.split("T")[1].split(":"))

sunset = data["results"]["sunset"]
# print(sunset)

timenow = dt.datetime.now()
# print(timenow)
