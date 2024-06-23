# main.py

from weather_forecast import WeatherForecast, WeatherData

def main():
    weather_data_handler = WeatherData()
    weather_forecast = WeatherForecast(weather_data_handler)
    
    while True:
        city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
        
        if city.lower() == 'exit':
            break
        
        forecast = weather_forecast.get_weather_forecast(city)
        print(forecast)

if __name__ == "__main__":
    main()
