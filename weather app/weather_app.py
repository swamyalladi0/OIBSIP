import requests
import sys

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city_name):
        params = {
            "q": city_name,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code != 200:
                print("\n❌ Error:", data.get("message", "Unable to fetch data"))
                return

            self.display_weather(data)

        except requests.exceptions.RequestException:
            print("\n⚠️ Network error. Please check your internet connection.")

    def display_weather(self, data):
        city = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        condition = data["weather"][0]["description"]

        print("\n" + "="*40)
        print(f"📍 Location: {city}, {country}")
        print(f"🌡️ Temperature: {temperature} °C")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬️ Wind Speed: {wind_speed} m/s")
        print(f"☁️ Condition: {condition.capitalize()}")
        print("="*40)


def main():
    print("\n🌦️ Welcome to SkyCast Weather App 🌦️")

    api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    app = WeatherApp(api_key)

    while True:
        city = input("\nEnter city name (or type 'exit' to quit): ").strip()

        if city.lower() == "exit":
            print("\nThank you for using SkyCast 👋")
            sys.exit()

        if not city:
            print("⚠️ City name cannot be empty.")
            continue

        app.get_weather(city)


if __name__ == "__main__":
    main()
