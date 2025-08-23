#!/usr/bin/env python3
#Author: Iddy Chesire
import typer
import platform
import socket
import psutil
from datetime import datetime
from rich.console import Console
from rich.table import Table
from .banners import sysmonitor_banner_panel

app = typer.Typer(help="SysMonitor - Cross-platform System Information Tool")
console = Console()

@app.callback(invoke_without_command=True)
def main(
    version: bool = typer.Option(False, "--version", help="Show version and exit"),
    style: str = typer.Option("panel", "--style", help="ascii | panel | big")
):
    if version:
        console.print("Sysmonitor v1.0.0")
        raise typer.Exit()

    if style == "ascii":
        print(sysmonitor_banner_ascii())
    elif style == "big":
        sysmonitor_banner_big()
    else:
        sysmonitor_banner_panel("v1.0.0")
        
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
    uname = platform.uname()
    data = {
        "Hostname": socket.gethostname(),
        "Node Name": uname.node,
        "OS": f"{uname.system} {uname.release}",
        "Version": uname.version,
        "Kernel": platform.version(),
        "Architecture": uname.machine,
        "Processor": uname.processor or "Unknown",
        "Boot Time": datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"),
        "Python Version": platform.python_version(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
    }
    print_table("Basic System Information", data)

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
    """Show memory usage (RAM)"""
    mem = psutil.virtual_memory()
    data = {
        "Total (MB)": mem.total // (1024**2),
        "Used (MB)": mem.used // (1024**2),
        "Free (MB)": mem.available // (1024**2),
    }
    print_table("Memory Information RAM (MB)", data)

@app.command()
def disk():
    """Show disk usage (SSD/HDD)"""
    table = Table(title="Disk Usage (SSD/HDD)", header_style="bold cyan")
    table.add_column("Device", style="dim")
    table.add_column("Mountpoint", style="cyan")
    table.add_column("Used", style="magenta")
    table.add_column("Total", style="green")
    table.add_column("Remaining",style="green")
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            table.add_row(
                part.device,
                part.mountpoint,
                f"{usage.used // (1024**3)} GB",
                f"{usage.total // (1024**3)} GB",
                f"{usage.free // (1024**3)} GB",
            )
        except PermissionError:
            continue
    console.print(table)

@app.command()
def network():
    """Show detailed network interfaces info"""
    table = Table(title="Network Interfaces", header_style="bold cyan")
    table.add_column("Interface", style="dim")
    table.add_column("IPv4", style="magenta")
    table.add_column("IPv6", style="green")
    table.add_column("MAC Address", style="yellow")
    table.add_column("MTU", style="cyan")
    table.add_column("Speed (Mbps)", style="bold blue")
    table.add_column("Status", style="bold")
    
    addrs = psutil.net_if_addrs()
    stats = psutil.net_if_stats()

    for name, addr_list in addrs.items():
        ipv4, ipv6, mac = "-", "-", "-"
        for s in addr_list:
            if s.family == socket.AF_INET:
                ipv4 = s.address
            elif s.family == socket.AF_INET6:
                ipv6 = s.address
            elif s.family == psutil.AF_LINK:  # MAC
                mac = s.address

        mtu = stats[name].mtu if name in stats else "-"
        speed = stats[name].speed if name in stats else "-"
        isup = "Up" if stats[name].isup else "Down" if name in stats else "?"

        table.add_row(name, ipv4, ipv6, mac, str(mtu), str(speed), isup)

    console.print(table)
@app.command()
def processes():
    """Show detailed running processes"""
    table = Table(title="Running Processes", header_style="bold cyan")
    table.add_column("PID", style="dim", width=8)
    table.add_column("Name", style="magenta")
    table.add_column("User", style="green")
    table.add_column("Status", style="yellow")
    table.add_column("CPU %", style="red", justify="right")
    table.add_column("Memory %", style="blue", justify="right")
    table.add_column("Threads", style="cyan", justify="right")
    table.add_column("Start Time", style="white")
    
    processes = sorted(processes, key=lambda proc: proc["cpu_percent"], reverse=True)[:15]
    for proc in psutil.process_iter(
        ["pid", "name", "username", "status", "cpu_percent", "memory_percent", "num_threads", "create_time"]
    ):
        try:
            start_time = datetime.fromtimestamp(proc.info["create_time"]).strftime("%Y-%m-%d %H:%M:%S")
            table.add_row(
                str(proc.info["pid"]),
                proc.info["name"] or "N/A",
                proc.info["username"] or "N/A",
                proc.info["status"],
                f"{proc.info['cpu_percent']:.1f}",
                f"{proc.info['memory_percent']:.1f}",
                str(proc.info["num_threads"]),
                start_time,
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    console.print(table)
@app.command()
def all():
    """Monitor all of the above"""
    console.rule("[bold green] System Monitor - Full Report [/bold green]")
    system()
    cpu()
    memory()
    disk()
    network()
    processes()
    console.rule("[bold green] End of Report [/bold green]")

if __name__ == "__main__":
    app()