"""
Ulan - Realm of 1001 Gods
Main entry point for the game
"""

from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Static
from textual.binding import Binding

class UlanApp(App):
    """Main application class for Ulan - Realm of 1001 Gods"""

    CSS = """
    Screen {
        align: center middle;
    }

    #welcome-container {
        width: 60;
        height: auto;
        border: solid green;
        padding: 2;
    }

    #title {
        text-align: center;
        text-style: bold;
        color: gold;
    }

    #subtitle {
        text-align: center;
        color: cyan;
        margin-top: 1;
    }

    #message {
        text-align: center;
        color: white;
        margin-top: 1;
    }
    """

    BINDINGS = [
        Binding("q", "quit", "Quit", show=True)
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield Container(
            Static("ULAN", id="title"),
            Static("Realm of 1001 Gods", id="subtitle"),
            Static("\nWelcome, mortal.\n\nYour environment is configured correctly.\nThe gods are watching...", id="message"), id="welcome-container"
        )
        yield Footer()

def main():
    app = UlanApp()
    app.run()

if __name__ == "__main__":
    main()