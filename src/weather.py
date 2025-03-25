import requests
# 修改前: from .config_loader import ConfigLoader
from src.config_loader import ConfigLoader  # 添加完整包路径

class WeatherFetcher:
    def __init__(self):
        self.config = ConfigLoader().get_weather_config()
    
    def get_weather(self, city, units='metric'):
        params = {
            'q': city,
            'appid': self.config['api_key'],
            'units': units  # 添加单位参数
        }
        
        try:
            response = requests.get(self.config['base_url'], params=params)
            response.raise_for_status()
            return self._parse_data(response.json())
        except requests.exceptions.RequestException as e:
            return f"Error fetching data: {str(e)}"
    
    def _parse_data(self, data):
        return {
            'city': data['name'],
            'temp': data['main']['temp'],
            'feels_like': data['main']['feels_like'],  # 新增体感温度
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],  # 新增风速
            'description': data['weather'][0]['description']
        }