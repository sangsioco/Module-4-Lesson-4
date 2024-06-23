# weather_forecast.py

class WeatherData:
    def __init__(self):
        # Simulated data based on city
        self.weather_data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
        }
    
    def fetch_weather_data(self, city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.weather_data.get(city, None)  # Return None if city not found

class WeatherForecast:
    def __init__(self, weather_data):
        self.weather_data = weather_data
    
    def parse_weather_data(self, data, city):
        # Function to parse weather data
        if not data:
            return f"Weather data not available for {city}"
        
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"
    
    def get_weather_forecast(self, city):
        # Function to provide weather forecast
        data = self.weather_data.fetch_weather_data(city)
        
        if not data:
            return f"Weather data not available for {city}"
        
        return self.parse_weather_data(data, city)

