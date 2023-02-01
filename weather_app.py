import os
import requests

if __name__ == '__main__':
    api_key_file = "api_key.txt"
    if os.path.exists(api_key_file):
        with open(api_key_file, "r") as f:
            api_key = f.read().strip()
    else:
        raise Exception("API key file not found")

def get_weather(location):
    api_key = open("api_key.txt").read().strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"
    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        #return None
        return {"error": "Sorry, no data available at this time"}
