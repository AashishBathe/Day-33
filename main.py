import requests
from datetime import datetime
# ISS code

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# long = response.json()["iss_position"]["longitude"]
# lat = response.json()["iss_position"]["latitude"]
# print((lat, long))

# Sunset Sunrise times API https://api.sunrise-sunset.org/json

parameters = {
    "lat": 19.085510,
    "lng": 73.021873,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()["results"]
sunrise = data["sunrise"].split("T")[1].split(":")[0]
sunset = data["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()
print(time_now.hour)
