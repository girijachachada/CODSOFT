import requests

# Function to get weather data from the OpenWeatherMap API
def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={location}&appid={api_key}&units=metric"  # Use metric units for temperature

    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

# Function to display weather information to the user
def display_weather(weather_data):
    if weather_data is not None:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]
        wind_speed = weather_data["wind"]["speed"]
        print()
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
        print(f"Wind Speed: {wind_speed} m/s")
        print()
    else:
        print("Weather data not available. Please check your location or try again later.")

if __name__ == "__main__":
    api_key = "0556cb920bcd67078dbdde76c6994629"  # Replace with your OpenWeatherMap API key
    print()
    location = input("Enter the name of a city or a zip code: ")

    weather_data = get_weather(api_key, location)

    display_weather(weather_data)
