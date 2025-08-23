#!/usr/bin/env python3
import typer
import platform
import socket
import psutil
from datetime import datetime
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="SysMonitor - Cross-platform System Information Tool")
console = Console()

def print_table(title, data: dict):
    table = Table(title=title, show_header=True, header_style="bold cyan")
    table.add_column("Metric", style="dim", width=20)
    table.add_column("Value", style="magenta")
    for k, v in data.items():
        table.add_row(str(k), str(v))
    console.print(table)

@app.command()
def system():
    """Show basic system information"""
    data = {
        "Hostname": socket.gethostname(),
        "OS": f"{platform.system()} {platform.release()}",
        "Kernel": platform.version(),
        "Architecture": platform.machine(),
        "Uptime": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
    }
    print_table("System Information", data)

@app.command()
def cpu():
    """Show CPU usage and details"""
    data = {
        "Cores": psutil.cpu_count(logical=True),
        "Usage %": f"{psutil.cpu_percent(interval=1)}%",
    }
    if hasattr(psutil, "getloadavg"):
        data["Load Avg"] = psutil.getloadavg()
    print_table("CPU Information", data)

@app.command()
def memory():
    """Show memory usage"""
    mem = psutil.virtual_memory()
    data = {
        "Total (MB)": mem.total // (1024**2),
        "Used (MB)": mem.used // (1024**2),
        "Free (MB)": mem.available // (1024**2),
    }
    print_table("Memory Information", data)

@app.command()
def disk():
    """Show disk usage"""
    table = Table(title="Disk Usage", header_style="bold cyan")
    table.add_column("Device", style="dim")
    table.add_column("Mountpoint", style="cyan")
    table.add_column("Used", style="magenta")
    table.add_column("Total", style="green")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            table.add_row(
                part.device,
                part.mountpoint,
                f"{usage.used // (1024**3)} GB",
                f"{usage.total // (1024**3)} GB",
            )
        except PermissionError:
            continue
    console.print(table)

@app.command()
def network():
    """Show network interfaces"""
    table = Table(title="Network Interfaces", header_style="bold cyan")
    table.add_column("Interface", style="dim")
    table.add_column("IP Address", style="magenta")
    for name, stats in psutil.net_if_addrs().items():
        for s in stats:
            if s.family == socket.AF_INET:
                table.add_row(name, s.address)
    console.print(table)

@app.command()
def processes():
    """Show top 5 processes by CPU"""
    table = Table(title="Top Processes (by CPU)", header_style="bold cyan")
    table.add_column("PID", style="dim")
    table.add_column("Name", style="magenta")
    table.add_column("CPU %", style="green")
    for p in sorted(psutil.process_iter(['pid','name','cpu_percent']),
                    key=lambda x: x.info['cpu_percent'], reverse=True)[:5]:
        table.add_row(str(p.info['pid']), p.info['name'], str(p.info['cpu_percent']))
    console.print(table)

if __name__ == "__main__":
    app()

def main():
    system()
    cpu()
    network()
    processes()
    
    console.print(table)