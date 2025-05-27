"""
This class represents a service to ask for weather data via an api from meteo
"""
import requests
class WeatherData:

    @classmethod
    def get_weather(cls,latitude, longitude):
        """
        gets weather data from meteo via its api with the given latitude and longitude for the location
        :param latitude: latitude for the weather data
        :param longitude: longitude for the weather data
        :return: temperature from the given location, weather mode as text
        """
        url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather = data["current_weather"]
            code = weather["weathercode"]
            weather_desc = cls.__convert_weathercode(code)
            return weather["temperature"], weather_desc


    @classmethod
    def __convert_weathercode(cls,code):
        """
        converts the weathercode from meteo to text
        codes can be found here https://open-meteo.com/en/docs#weather_variable_documentation
        :param code: the code to convert to text
        :return: the weather mode as text
        """
        match code:
            case 0:
                return "Clear sky"
            case 1:
                return "Mainly clear"
            case 2:
                return "Partly cloudy"
            case 3:
                return "Overcast"
            case 45:
                return "Fog"
            case 48:
                return "Depositing rime fog"
            case 51:
                return "Drizzle: Light intensity"
            case 53:
                return "Drizzle: Moderate intensity"
            case 55:
                return "Drizzle: Dense intensity"
            case 56:
                return "Freezing Drizzle: Light intensity"
            case 57:
                return "Freezing Drizzle: Dense intensity"
            case 61:
                return "Rain: Slight intensity"
            case 63:
                return "Rain: Moderate intensity"
            case 65:
                return "Rain: Heavy intensity"
            case 66:
                return "Freezing Rain: Light intensity"
            case 67:
                return "Freezing Rain: Heavy intensity"
            case 71:
                return "Snow fall: Slight intensity"
            case 73:
                return "Snow fall: Moderate intensity"
            case 75:
                return "Snow fall: Heavy intensity"
            case 77:
                return "Snow grains"
            case 80:
                return "Rain showers: Slight"
            case 81:
                return "Rain showers: Moderate"
            case 82:
                return "Rain showers: Violent"
            case 85:
                return "Snow showers: Slight"
            case 86:
                return "Snow showers: Heavy"
            case 95:
                return "Thunderstorm: Slight or moderate"
            case 96:
                return "Thunderstorm with slight hail"
            case 99:
                return "Thunderstorm with heavy hail"
            case _:
                return "Unknown weather code"





