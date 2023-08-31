import requests
from env_var import api


def get_coords(city):

    url_api = f"https://api.openweathermap.org/geo/1.0/direct?q={city}&appid={api}"

    response = requests.get(url_api)

    if response.status_code == 200:
            data = response.json()
            lat = data[0].get("lat")
            lon = data[0].get("lon")
            return lat, lon

    else:
        print(f"Error:{response.status_code}")
        return None, None


def get_weather(lat, lon):
    url_api = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api}"

    response = requests.get(url_api)

    if response.status_code == 200:
            data = response.json()
            weather = data["weather"][0]["description"]
            main = data["main"]
            cloud = data["clouds"]["all"]
            return weather, main, cloud

    else:
        print(f"Error:{response.status_code}")
        return None

print(get_coords("Lyon"))
