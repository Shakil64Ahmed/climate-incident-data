import requests
import datetime

# Replace with your OpenWeatherMap API key
API_KEY = 'your_openweathermap_api_key_here'

# OpenWeatherMap API endpoint for historical data
BASE_URL = 'https://api.openweathermap.org/data/3.0/onecall/timemachine'

# Define parameters for the API request
params = {
    'lat': 39.113014,  # Latitude for a location in the USA (e.g., Kansas City)
    'lon': -94.626469,  # Longitude for a location in the USA (e.g., Kansas City)
    'dt': int(datetime.datetime(2020, 1, 1).timestamp()),  # Unix timestamp for 2020-01-01
    'units': 'metric',  # Use metric units
    'appid': API_KEY
}

# Make the API request
response = requests.get(BASE_URL, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print("Data fetched successfully!")
    print(data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print(response.text)