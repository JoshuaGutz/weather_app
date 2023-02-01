import os
import requests

def get_temperature(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=imperial"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        raise Exception("Failed to retrieve weather information")

if __name__ == '__main__':
    api_key_file = "api_key.txt"
    if os.path.exists(api_key_file):
        with open(api_key_file, "r") as f:
            api_key = f.read().strip()
    else:
        raise Exception("API key file not found")
    city = "London"
    temperature = get_temperature(api_key, city)
    print(f"The current temperature in {city} is {temperature}")

def get_weather(location):
    api_key = open("api_key.txt").read().strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": "Sorry, no data available at this time"}
