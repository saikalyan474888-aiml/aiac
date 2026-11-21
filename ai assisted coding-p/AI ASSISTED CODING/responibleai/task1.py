import json
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen

API_KEY = input("Enter your OpenWeather API key: ")
CITY = "Hyderabad"

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": CITY,
    "appid": API_KEY,
    "units": "metric"
}

try:
    request_url = f"{url}?{urlencode(params)}"
    with urlopen(request_url) as response:
        data = json.load(response)
    print("City:", CITY)
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
except HTTPError as error:
    try:
        details = json.load(error)
        message = details.get("message", "Unable to fetch weather data")
    except (json.JSONDecodeError, UnicodeDecodeError):
        message = "Unable to fetch weather data"
    print("Error:", message)
except URLError as error:
    print("Error:", error.reason)