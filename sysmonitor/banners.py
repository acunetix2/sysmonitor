from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

console = Console()

def sysmonitor_banner_panel(version: str = "v1.0.0"):
    title = Text("SYSMONITOR", justify="center", style="bold cyan")
    sub   = Text(f"System Insights • {version}", justify="center", style="dim")
    body  = Text.from_markup(
        "[bold]CPU[/bold] • [bold]MEM[/bold] • [bold]DISK[/bold] • [bold]NET[/bold] • [bold]PROC[/bold]",
        justify="center"
    )
    panel_text = Text.assemble(title, "\n", sub, "\n\n", body)
    console.print(Panel(panel_text, box=box.HEAVY, border_style="cyan", padding=(1,3)))
