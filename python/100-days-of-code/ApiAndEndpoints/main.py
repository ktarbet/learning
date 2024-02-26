import requests
from datetime import datetime

# Juneau, AK
LAT = 58.259269
LONG = -134.434204

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = datetime.fromisoformat(data["results"]["sunrise"])
sunset = datetime.fromisoformat(data["results"]["sunset"])

time_now = datetime.now()


def is_iss_close():
    return abs(iss_latitude - LAT) < 5 and abs(iss_longitude - LONG) < 5


def is_daytime():
    return time_now > sunrise and time_now < sunset

if is_iss_close() and not is_daytime():
    print("it is close")

