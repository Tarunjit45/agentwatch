from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Log
from textual.containers import Grid
import psutil
import random

class AgentWatch(App):
    CSS = """
    Grid {
        grid-size: 2;
        grid-columns: 2fr 1fr;
        padding: 1;
    }
    #log-panel { border: double cyan; height: 100%; }
    #stats-panel { border: heavy magenta; padding: 1; }
    """

    def compose(self) -> ComposeResult:
        yield Header(show_clock=True)
        with Grid():
            yield Log(id="log-panel")
            with Static(id="stats-panel"):
                yield Static("💻 System Health: OK", id="cpu")
                yield Static("🔢 Tokens: 0", id="tokens")
                yield Static("💸 Cost: $0.00", id="cost")
        yield Footer()

    def on_mount(self) -> None:
        self.tokens = 0
        self.set_interval(1, self.tick)
        self.query_one("#log-panel").write_line("🚀 AgentWatch is live...")

    def tick(self) -> None:
        # Update Stats
        self.tokens += random.randint(10, 100)
        cost = (self.tokens / 1000) * 0.02
        cpu = psutil.cpu_percent()
        
        self.query_one("#cpu").update(f"💻 CPU Usage: {cpu}%")
        self.query_one("#tokens").update(f"🔢 Tokens: {self.tokens}")
        self.query_one("#cost").update(f"💸 Cost: [green]${cost:.4f}[/]")
        
        if random.random() > 0.8:
            self.query_one("#log-panel").write_line(f"Agent action: Analyzing file...")

if __name__ == "__main__":
    AgentWatch().run()