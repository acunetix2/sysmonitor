# SysMonitor

A **cross-platform CLI tool** to collect **system and resource usage information** such as CPU, memory, disk, network, and running processes. Built with **Python**, powered by `psutil`, `typer`, and `rich`.
**Author:** **Iddy Chesire**
---

## Features

* **System Info**: OS, hostname, architecture, boot time
* **CPU Usage**: per-core load, frequency
* **Memory**: total, used, available
* **Disk**: usage, free/remaining space
* **Network**: interfaces, IPs, traffic stats
* **Processes**: top processes, CPU/memory usage
* **All-in-One View**: show everything in a single formatted table

---

## Controlled Environment Setup

SysMonitor works on **Linux**, **macOS**, and **Windows**.
To ensure consistent results, it’s recommended to run in a **Python virtual environment**.

### Prerequisites

* Python **3.7+** installed
* Git (optional, for cloning repo)

---

### Linux / macOS

```bash
# Clone repo
git clone https://github.com/acunetix2/sysmonitor.git
cd sysmonitor

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -e .
```

Run with:

```bash
sysmonitor --help
```

Deactivate environment when done:

```bash
deactivate
```

---

### Windows (PowerShell / CMD)

```powershell
# Clone repo
git clone https://github.com/acunetix2/sysmonitor.git
cd sysmonitor

# Create and activate virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -e .
```

Run with:

```powershell
sysmonitor --help
```

Deactivate environment when done:

```powershell
deactivate
```

---

## Usage

List available commands:

```bash
sysmonitor --help
```

Example commands:

```bash
sysmonitor system      # System info
sysmonitor cpu         # CPU usage
sysmonitor memory      # Memory stats
sysmonitor disk        # Disk usage
sysmonitor network     # Network info
sysmonitor processes   # Running processes
sysmonitor all         # Print everything in one view
```


---

## 📄 License

MIT License © 2025 \[Iddy Chesire]
