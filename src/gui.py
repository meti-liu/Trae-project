import tkinter as tk
from tkinter import ttk
from .weather import WeatherFetcher

class WeatherApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("天气预报")
        self.geometry("400x300")
        self.fetcher = WeatherFetcher()
        self._create_widgets()
    
    def _create_widgets(self):
        # 输入框区域
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)
        
        self.city_entry = ttk.Entry(self.input_frame, width=20)
        self.city_entry.pack(side=tk.LEFT, padx=5)
        
        self.unit_var = tk.StringVar(value="metric")
        self.unit_combobox = ttk.Combobox(self.input_frame, 
                                       textvariable=self.unit_var,
                                       values=["metric", "imperial"],
                                       width=8,
                                       state="readonly")
        self.unit_combobox.pack(side=tk.LEFT, padx=5)
        
        self.search_btn = ttk.Button(self.input_frame, 
                                   text="查询", 
                                   command=self.get_weather)
        self.search_btn.pack(side=tk.LEFT, padx=5)
        
        # 结果显示区域
        self.result_frame = ttk.LabelFrame(self, text="天气信息")
        self.result_frame.pack(fill=tk.BOTH, expand=True, padx=10)
        
        self.result_labels = {
            'temp': ttk.Label(self.result_frame, text="温度: "),
            'feels_like': ttk.Label(self.result_frame, text="体感: "),
            'humidity': ttk.Label(self.result_frame, text="湿度: "),
            'wind_speed': ttk.Label(self.result_frame, text="风速: "),
            'description': ttk.Label(self.result_frame, text="天气: ")
        }
        
        for label in self.result_labels.values():
            label.pack(anchor=tk.W, padx=10, pady=2)
    
    def get_weather(self):
        city = self.city_entry.get()
        units = self.unit_var.get()
        
        result = self.fetcher.get_weather(city, units)
        if isinstance(result, dict):
            unit_symbol = '°C' if units == 'metric' else '°F'
            self.result_labels['temp'].config(text=f"温度: {result['temp']}{unit_symbol}")
            self.result_labels['feels_like'].config(text=f"体感: {result['feels_like']}{unit_symbol}")
            self.result_labels['humidity'].config(text=f"湿度: {result['humidity']}%")
            self.result_labels['wind_speed'].config(text=f"风速: {result['wind_speed']} m/s")
            self.result_labels['description'].config(text=f"天气: {result['description']}")
        else:
            self.show_error(result)
    
    def show_error(self, message):
        error_window = tk.Toplevel(self)
        error_window.title("错误")
        ttk.Label(error_window, text=message, foreground="red").pack(padx=20, pady=10)
        ttk.Button(error_window, text="确定", command=error_window.destroy).pack(pady=5)

def start_gui():
    app = WeatherApp()
    app.mainloop()