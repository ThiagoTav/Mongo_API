# models.py

from datetime import datetime

class WeatherEntity:

    def __init__(self, temperature, date, city='', atmosphericPressure='', humidity='', weather='') -> None:
        self.temperature = temperature
        self.city = city
        self.atmosphericPressure = atmosphericPressure
        self.humidity = humidity
        self.weather = weather
        self.date = date

    def to_dict(self):
        return {
            "temperature": self.temperature,
            "city": self.city,
            "atmosphericPressure": self.atmosphericPressure,
            "humidity": self.humidity,
            "weather": self.weather,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S")
        }