import json

import requests
import os


class OpenWeather:
    def __init__(self, lat: float, lon: float):
        self.lat = lat
        self.lon = lon
        self.api_key = os.getenv("API_KEY")

    def get_3_hour_forecast(self, count=1):
        """
        Gets forecast data in 3 hour increments
        Args:
           count: number of time-steps (each is 3 hours apart)
        Returns:

       """
        args = {"lat": self.lat,
                "lon": self.lon,
                "cnt": count,
                "appid": self.api_key
                }
        response = requests.get("https://api.openweathermap.org/data/2.5/forecast", args)
        response.raise_for_status()
        print(f"response code:{response.status_code}")
        data = response.json()
        return data


def get_id_list_from_weather(weather):
    list = [item["id"] for item in weather]
    return list


def get_ts_of_weather_id(forecast):
    """
    Args:
        forecast:
    Returns:
{'2024-03-03 00:00:00': [802], '2024-03-03 03:00:00': [803], '2024-03-03 06:00:00': [803], '2024-03-03 09:00:00': [804]}
    """
    list = forecast["list"]
    # short_names = [sn for sn in names if len(sn) <= 4]
    weather_ts = {ts["dt_txt"]: get_id_list_from_weather(ts["weather"]) for ts in list}
    print(weather_ts)
    return weather_ts


def min_weather_code(ts):
    list_of_lists = ts.values()
    combined_list = [item for sublist in list_of_lists for item in sublist]
    return min(combined_list)


def test():
    api = OpenWeather(44.34, 10.99)
    f = api.get_3_hour_forecast(4)
    ts = get_ts_of_weather_id(f)
    min_code = min_weather_code(ts)
    if min_code < 700:
        print("Bring an umbrella")
    print(f"min code = {min_code}")
    # print(json.dumps(f, indent=4))


test()
