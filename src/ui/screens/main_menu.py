from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.widgets import Static, Button
from textual.binding import Binding
from textual.screen import Screen

# import other screens for navigation
from src.ui.screens.character_creation import CharacterCreationScreen

class MainMenuScreen(Screen):
    CSS = """
    MainMenuScreen {
        align: center middle;
    }
    
    #menu-container {
        width: 60;
        height: auto;
        border: double gold;
        padding: 2;
    }
    
    #title {
        text-align: center;
        text-style: bold;
        color: gold;
        margin-bottom: 1;
    }
    
    #subtitle {
        text-align: center;
        color: cyan;
        margin-bottom: 2;
    }
    
    #menu-options {
        align: center middle;
        width: 100%;
        height: auto;
    }
    
    Button {
        width: 30;
        margin: 1;
    }
    
    #flavor {
        text-align: center;
        color: #888888;
        text-style: italic;
        margin-top: 2;
    }
    """

    BINDINGS = [
        Binding("n", "new_game", "New Game", show=True),
        Binding("q", "quit", "Quit", show=True),
    ]
    
 def compose(self) -> ComposeResult:
        """Create main menu UI"""
        yield Container(
            Static("ULAN", id="title"),
            Static("Realm of 1001 Gods", id="subtitle"),
            Vertical(
                Button("New Game", id="new-game", variant="primary"),
                Button("Load Game", id="load-game", disabled=True),
                Button("Settings", id="settings", disabled=True),
                Button("Quit", id="quit-btn", variant="error"),
                id="menu-options"
            ),
            Static("The gods await your arrival...", id="flavor"),
            id="menu-container"
        )
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button clicks"""
        if event.button.id == "new-game":
            self.action_new_game()
        elif event.button.id == "quit-btn":
            self.app.exit()
    
    def action_new_game(self) -> None:
        """Start character creation"""
        self.app.push_screen(CharacterCreationScreen())
    
    def action_quit(self) -> None:
        """Quit the game"""
        self.app.exit()