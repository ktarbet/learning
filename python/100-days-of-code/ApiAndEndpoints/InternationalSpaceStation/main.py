import time

import requests
from datetime import datetime


class ISS:
    """
    gets the Location of International Space Station
    """

    def __init__(self):
        r = requests.get(url="http://api.open-notify.org/iss-now.json")
        r.raise_for_status()
        data = r.json()

        self.latitude = float(data["iss_position"]["latitude"])
        self.longitude = float(data["iss_position"]["longitude"])
        print(f"iss lat, long: {self.latitude}, {self.longitude}")


class Sun:
    """
    Sun gets sunrise and sunset for a lat,log location
    """

    def __init__(self, lat, long):
        parameters = {
            "lat": lat,
            "lng": long,
            "formatted": 0,
        }
        response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
        response.raise_for_status()
        data = response.json()
        self.sunrise = datetime.fromisoformat(data["results"]["sunrise"])
        self.sunset = datetime.fromisoformat(data["results"]["sunset"])
        print(f"sunrise is {self.sunrise},  sunset is {self.sunset}")


# Juneau, AK
LAT = 58.259269
LONG = -134.434204


def is_iss_close():
    iss = ISS()
    return abs(iss.latitude - LAT) < 5 and abs(iss.longitude - LONG) < 5


def is_daytime(sun):
    time_now = datetime.now()
    return time_now > sun.sunrise and time_now < sun.sunset


sun = Sun(LAT, LONG)

while True:

    if is_iss_close() and not is_daytime(sun):
        print("it is close")

    time.sleep(10)
