# 🌦️ Python 天气预报系统（命令行 + GUI 双模式）

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-lightgrey)

基于 OpenWeatherMap API 开发的天气查询工具，支持 **命令行 + 图形界面** 双模式交互，提供实时温度、体感、湿度、风速与天气描述等关键数据。

---

## 🚀 核心功能

- 📟 **双模交互**：CLI 命令行快速查询 + Tkinter 图形界面交互
- 🌍 **全球覆盖**：支持全球 20,000+ 城市天气数据获取
- ⚙️ **配置中心**：使用 INI 文件管理 API 密钥与服务端点
- 🛡️ **异常处理**：覆盖网络失败、数据缺失、配置异常等多种错误
- 🌡️ **单位切换**：摄氏度（metric）与华氏度（imperial）一键切换

---

## 🛠️ 技术架构

| 模块         | 技术实现                   |
|--------------|----------------------------|
| API 交互     | Requests + JSON 解析       |
| 配置管理     | configparser + INI 文件    |
| 命令行界面   | argparse + 参数校验        |
| 图形界面     | Tkinter + 响应式布局       |
| 异常处理     | try-except 全流程错误管理  |

---

## 📁 项目结构


