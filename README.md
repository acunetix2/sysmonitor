# 🖥️ SysMonitor

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Tests](https://github.com/yourusername/sysmonitor/actions/workflows/tests.yml/badge.svg)](https://github.com/yourusername/sysmonitor/actions)

> **SysMonitor** is a cross-platform CLI tool to collect **system information** and **resource usage stats** (CPU, memory, disk, network, processes).  
It works on **Linux, Windows, and macOS** using `psutil`, `typer`, and `rich`.

---

## ✨ Features
- 📊 System info: hostname, OS, kernel, uptime
- 🖥️ CPU: cores, usage, load average
- 💾 Memory: total, used, free
- 📂 Disk usage: per partition
- 🌐 Network interfaces & IPs
- 🔎 Top processes by CPU
- 🎨 Pretty colored tables (thanks to [Rich](https://github.com/Textualize/rich))

---

## 📦 Installation

### Clone & Install
```bash
git clone https://github.com/acunetix2/sysmonitor.git
cd sysmonitor
pip install -e .

🚀 Usage

After installation, run:

sysmonitor system
sysmonitor cpu
sysmonitor memory
sysmonitor disk
sysmonitor network
sysmonitor processes