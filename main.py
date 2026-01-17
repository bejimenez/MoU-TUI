"""
Ulan - Realm of 1001 Gods
Main entry point for the game.
"""

from textual.app import App
from textual.binding import Binding

from src.ui.screens.main_menu import MainMenuScreen

class UlanApp(App):
    BINDINGS = [
        Binding("q", "quit", "Quit the game", show=True),
    ]

    def on_mount(self) -> None:
        self.push_screen(MainMenuScreen())

def main():
    app = UlanApp()
    app.run()

if __name__ == "__main__":
    main()