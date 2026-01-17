from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical
from textual.widgets import Static, Input, Label
from textual.binding import Binding

# import other screens for navigation
# from src.ui.screens.game_view import GameViewScreen

class CharacterCreationScreen(Screen):
    """Character creation screen - Phase 1: Name input only"""
    
    CSS = """
    CharacterCreationScreen {
        align: center middle;
    }
    
    #creation-container {
        width: 70;
        height: 25;
        border: double gold;
        padding: 1;
    }
    
    #header {
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
    
    #prompt {
        margin-top: 2;
        margin-bottom: 1;
        color: white;
    }
    
    #name-input {
        margin-bottom: 1;
    }
    
    #flavor-text {
        margin-top: 2;
        color: #888888;
        text-align: center;
        text-style: italic;
    }
    
    #instructions {
        margin-top: 2;
        color: #aaaaaa;
        text-align: center;
    }
    """
    
    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
    ]
    
    def compose(self) -> ComposeResult:
        """Create the character creation UI"""
        yield Container(
            Static("ULAN - CHARACTER CREATION", id="header"),
            Static("Realm of 1001 Gods", id="subtitle"),
            Static("What shall the mortals call you?", id="prompt"),
            Input(
                placeholder="Enter your name...",
                max_length=30,
                id="name-input"
            ),
            Static(
                "Your name echoes through the realm. Choose one that\n"
                "strikes fear into your enemies and inspires your allies.",
                id="flavor-text"
            ),
            Static(
                "[ENTER] Begin Your Journey  [ESC] Return to Menu",
                id="instructions"
            ),
            id="creation-container"
        )
    
    def on_mount(self) -> None:
        """Focus the input when screen loads"""
        self.query_one(Input).focus()
    
    def on_input_submitted(self, event: Input.Submitted) -> None:
        """Handle when player presses Enter in the name input"""
        name = event.value.strip()
        
        if not name:
            self.notify("You must enter a name!", severity="warning")
            return
        
        # TODO: For now, just show a notification. Later we'll transition to game
        self.notify(f"Welcome, {name}! (Game screen coming soon...)")
    
    def action_cancel(self) -> None:
        """Return to main menu"""
        self.app.pop_screen()