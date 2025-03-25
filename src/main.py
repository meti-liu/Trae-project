import argparse
from src.weather import WeatherFetcher
from src.gui import start_gui  # 新增导入

def main():
    parser = argparse.ArgumentParser(description='天气预报程序')
    parser.add_argument('--gui', action='store_true', help='启动图形界面')
    parser.add_argument('city', nargs='?', type=str, help='城市名称（命令行模式必填）')
    parser.add_argument('--units', '-u', choices=['metric', 'imperial'], 
                        default='metric', help='温度单位')
    args = parser.parse_args()

    if args.gui:
        start_gui()  # 新增GUI启动分支
    else:
        fetcher = WeatherFetcher()
        result = fetcher.get_weather(args.city, args.units)
        
        if isinstance(result, dict):
            print(f"Weather in {result['city']}:")
            print(f"Temperature: {result['temp']}°{'C' if args.units == 'metric' else 'F'}")
            print(f"Feels like: {result['feels_like']}°{'C' if args.units == 'metric' else 'F'}")
            print(f"Humidity: {result['humidity']}%")
            print(f"Wind Speed: {result['wind_speed']} m/s")
            print(f"Conditions: {result['description']}")
        else:
            print(result)

if __name__ == "__main__":
    main()