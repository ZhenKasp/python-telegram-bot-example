import datetime

class DataPreparerService:
    def parse_time(self, time):
        return datetime.datetime.fromtimestamp(time)

    def temperature_data(self, temp_max, temp_min):
        if temp_max == temp_min:
            return (f"Temperature - {temp_max}\n")
        else:
            return (f"Max temperature - {temp_max}\n"
                    f"Min temperature - {temp_min}\n")

    def wind_direction_data(self, degrees):
        directions = ['↑ N', '↗ NE', '→ E', '↘ SE', '↓ S', '↙ SW', '← W', '↖ NW'];
        return directions[round(degrees / 45) % 8];

    def prepare_weather_data(self, data):
        output = (f"{self.temperature_data(data['main']['temp_max'], data['main']['temp_min'])}"
                  f"Feels like - {data['main']['feels_like']}\n"
                  f"{data['weather'][0]['description'].capitalize()}\n"
                  f"Humidity - {data['main']['humidity']}%\n"
                  "\n"
                  f"Sunrise - {self.parse_time(data['sys']['sunrise'])}\n"
                  f"Sunset - {self.parse_time(data['sys']['sunset'])}\n"
                  "\n"
                  f"Wind - {data['wind']['speed']} m/s {self.wind_direction_data(data['wind']['deg'])}\n")

        return output