import requests
from datetime import datetime, timezone
import smtplib


MY_LAT = 19.075983  # Your latitude
MY_LONG = 72.877655  # Your longitude

EMAIL = "randommail@gmail.com"
PASS = "password"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def close_to_me():
    if (67 <= iss_longitude <= 77) and (14 <= iss_latitude <= 24):
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now(timezone.utc)


if close_to_me() and (time_now.hour >= sunset or time_now.hour <= sunrise):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASS)
        connection.sendmail(from_addr=EMAIL, to_addrs=EMAIL, msg=f"Subject: ISS OVERHEAD!\n\nLOOK UP")



