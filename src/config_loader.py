import configparser
from pathlib import Path

# 无需修改此文件，保持原有实现
class ConfigLoader:
    def __init__(self):
        self.config = configparser.ConfigParser()
        config_path = Path(__file__).parent.parent / 'config/settings.ini'
        self.config.read(config_path)
    
    def get_weather_config(self):
        return {
            'api_key': self.config['OpenWeather']['api_key'],
            'base_url': self.config['OpenWeather']['base_url']
        }