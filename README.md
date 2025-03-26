# 🌦️ Python天气预报系统

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)

基于OpenWeatherMap API开发的天气查询工具，支持命令行与图形界面双模式交互，提供实时温度/湿度/风速等核心数据。

---

## 🚀 核心功能

- 📟 **双模交互**：CLI命令行快速查询 + Tkinter图形界面
- 🌍 **全球覆盖**：支持20,000+城市实时天气数据获取
- ⚙️ **配置中心**：INI文件管理API密钥与服务端点
- 🛡️ **异常处理**：网络请求/数据解析/配置加载全流程容错
- 🔄 **单位转换**：摄氏度与华氏度一键切换

---

## 🛠️ 技术架构

| 模块         | 技术实现                 |
|--------------|--------------------------|
| API交互      | Requests + JSON解析      |
| 配置管理     | configparser + Pathlib   |
| 命令行界面   | argparse + 参数校验     |
| 图形界面     | Tkinter + 响应式布局     |
| 数据处理     | 类封装 + 数据字典转换    |

