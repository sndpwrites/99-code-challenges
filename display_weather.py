import requests

def load_api_key(file_path):
    """Load API key from a file."""
    with open(file_path, 'r') as file:
        return file.read().strip()

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }e
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        weather_data = response.json()
        
        # Extract weather information
        temperature = weather_data['main']['temp']
        weather_description = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']
        wind_speed = weather_data['wind']['speed']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {weather_description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

if __name__ == "__main__":
    api_key_file = "config.txt"  # File where API key is stored
    api_key = load_api_key(api_key_file)
    
    city = input("Enter the city name: ")
    get_weather(city, api_key)