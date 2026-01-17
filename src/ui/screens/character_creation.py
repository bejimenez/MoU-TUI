from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Vertical, Horizontal, Center
from textual.widgets import (
    Static, Input, Label, Button, TabbedContent, TabPane
)
from textual.binding import Binding
import random

from src.game.character import Character


class CharacterCreationScreen(Screen):
    """Tabbed character creation screen with name, attributes, fervor, and review"""
    
    CSS = """
    CharacterCreationScreen {
        align: center middle;
    }
    
    #creation-container {
        width: 90;
        height: 35;
        border: double gold;
        padding: 1;
    }
    
    #header {
        text-align: center;
        text-style: bold;
        color: gold;
        margin-bottom: 1;
    }
    
    .section-title {
        text-align: center;
        color: cyan;
        margin-bottom: 1;
        text-style: bold;
    }
    
    .flavor-text {
        color: #888888;
        text-align: center;
        text-style: italic;
        margin-top: 1;
        margin-bottom: 1;
    }
    
    .stat-row {
        height: 3;
        margin: 0 2;
    }
    
    .stat-label {
        width: 16;
        content-align: center middle;
    }
    
    .stat-value {
        width: 8;
        content-align: center middle;
        text-style: bold;
        color: cyan;
    }
    
    .stat-button {
        width: 5;
        min-width: 5;
    }
    
    #points-display {
        text-align: center;
        color: yellow;
        text-style: bold;
        margin: 1;
    }
    
    #randomize-btn {
        margin: 1;
    }
    
    #fervor-display {
        text-align: center;
        color: cyan;
        text-style: bold;
        margin: 1;
    }
    
    .fervor-button {
        width: 10;
        margin: 0 1;
    }
    
    #navigation {
        margin-top: 1;
        height: 3;
    }
    
    .nav-button {
        margin: 0 1;
    }
    """
    
    BINDINGS = [
        Binding("escape", "cancel", "Cancel", show=True),
        Binding("ctrl+n", "next_tab", "Next", show=False),
        Binding("ctrl+p", "prev_tab", "Previous", show=False),
    ]
    
    def __init__(self):
        super().__init__()
        self.character = Character()
    
    def compose(self) -> ComposeResult:
        """Create the tabbed character creation UI"""
        with Container(id="creation-container"):
            yield Static("ULAN - CHARACTER CREATION", id="header")
            
            with TabbedContent(initial="name-tab"):
                # TAB 1: Name
                with TabPane("Name", id="name-tab"):
                    yield Static("What shall the mortals call you?", classes="section-title")
                    yield Input(
                        placeholder="Enter your name...",
                        max_length=30,
                        id="name-input"
                    )
                    yield Static(
                        "Your name echoes through the realm. Choose one that\n"
                        "strikes fear into your enemies and inspires your allies.",
                        classes="flavor-text"
                    )
                
                # TAB 2: Attributes
                with TabPane("Attributes", id="attr-tab"):
                    yield Static("Distribute Your Abilities", classes="section-title")
                    yield Static(id="points-display")
                    yield Center(Button("Randomize Stats", id="randomize-btn", variant="primary"))
                    
                    # Create stat rows
                    for stat in ["strength", "dexterity", "constitution", 
                                "intelligence", "wisdom", "charisma"]:
                        with Horizontal(classes="stat-row"):
                            yield Label(stat.capitalize(), classes="stat-label")
                            yield Button("-", classes=f"stat-button stat-minus", id=f"{stat}-minus")
                            yield Static("8", classes="stat-value", id=f"{stat}-value")
                            yield Button("+", classes=f"stat-button stat-plus", id=f"{stat}-plus")
                    
                    yield Static(
                        "Point-Buy System: 27 points total. Stats range from 8-15.\n"
                        "Higher stats cost more points (13→14 costs 2, 14→15 costs 2).",
                        classes="flavor-text"
                    )
                
                # TAB 3: Divine Fervor
                with TabPane("Divine Fervor", id="fervor-tab"):
                    yield Static("Choose Your Zealotry", classes="section-title")
                    yield Static(id="fervor-display")
                    
                    with Center():
                        with Horizontal():
                            yield Button("<<", classes="fervor-button", id="fervor-min")
                            yield Button("-", classes="fervor-button", id="fervor-minus")
                            yield Button("+", classes="fervor-button", id="fervor-plus")
                            yield Button(">>", classes="fervor-button", id="fervor-max")
                    
                    yield Static(id="fervor-description")
                    yield Static(
                        "Divine Fervor determines how quickly you gain loyalty with gods.\n"
                        "High Fervor = Rapid devotion but locked into fewer gods\n"
                        "Low Fervor = Slow devotion but flexibility with multiple gods",
                        classes="flavor-text"
                    )
                
                # TAB 4: Review
                with TabPane("Review", id="review-tab"):
                    yield Static("Your Character", classes="section-title")
                    yield Static(id="review-content")
                    yield Static(
                        "Review your choices. Return to previous tabs to make changes.",
                        classes="flavor-text"
                    )
            
            # Navigation buttons at bottom
            with Center(id="navigation"):
                with Horizontal():
                    yield Button("← Back to Menu", id="cancel-btn", classes="nav-button")
                    yield Button("Begin Journey →", id="confirm-btn", 
                               variant="success", classes="nav-button")
    
    def on_mount(self) -> None:
        """Initialize the screen"""
        self.query_one(Input).focus()
        self.update_points_display()
        self.update_fervor_display()
    
    def update_points_display(self) -> None:
        """Update the points remaining display"""
        points = self.character.points_remaining
        color = "green" if points >= 0 else "red"
        self.query_one("#points-display").update(
            f"[{color}]Points Remaining: {points} / 27[/{color}]"
        )
    
    def update_stat_display(self, stat_name: str) -> None:
        """Update a single stat value display"""
        value = getattr(self.character, stat_name)
        self.query_one(f"#{stat_name}-value").update(str(value))
    
    def update_all_stat_displays(self) -> None:
        """Update all stat displays"""
        for stat in ["strength", "dexterity", "constitution", 
                    "intelligence", "wisdom", "charisma"]:
            self.update_stat_display(stat)
        self.update_points_display()
    
    def update_fervor_display(self) -> None:
        """Update the Divine Fervor display"""
        fervor = self.character.divine_fervor
        self.query_one("#fervor-display").update(
            f"Divine Fervor: {fervor} / 10"
        )
        
        # Update description based on fervor level
        desc = self.query_one("#fervor-description")
        if fervor <= 3:
            desc.update(
                "[cyan]Pragmatic Soul:[/cyan] You approach the gods with caution.\n"
                "Loyalty builds slowly, but you remain free to serve many masters."
            )
        elif fervor <= 6:
            desc.update(
                "[cyan]Balanced Devotion:[/cyan] You walk the middle path.\n"
                "Neither fanatic nor skeptic, you can adapt as needed."
            )
        else:
            desc.update(
                "[cyan]Zealous Heart:[/cyan] Faith burns bright within you.\n"
                "Your devotion grows swiftly, but you struggle to serve conflicting gods."
            )
    
    def update_review(self) -> None:
        """Update the review tab content"""
        char = self.character
        review_text = f"""
[bold cyan]Name:[/bold cyan] {char.name if char.name else "[red]Not Set[/red]"}

[bold cyan]Attributes:[/bold cyan]
  Strength:     {char.strength}
  Dexterity:    {char.dexterity}
  Constitution: {char.constitution}
  Intelligence: {char.intelligence}
  Wisdom:       {char.wisdom}
  Charisma:     {char.charisma}

[bold cyan]Divine Fervor:[/bold cyan] {char.divine_fervor} / 10

[bold yellow]Points Used:[/bold yellow] {char.points_spent} / 27
"""
        self.query_one("#review-content").update(review_text)
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle all button presses"""
        button_id = event.button.id
        
        # Stat adjustment buttons
        if button_id and "-minus" in button_id:
            stat_name = button_id.replace("-minus", "")
            if self.character.can_decrease_stat(stat_name):
                current = getattr(self.character, stat_name)
                setattr(self.character, stat_name, current - 1)
                self.update_stat_display(stat_name)
                self.update_points_display()
        
        elif button_id and "-plus" in button_id:
            stat_name = button_id.replace("-plus", "")
            if self.character.can_increase_stat(stat_name):
                current = getattr(self.character, stat_name)
                setattr(self.character, stat_name, current + 1)
                self.update_stat_display(stat_name)
                self.update_points_display()
        
        # Randomize button
        elif button_id == "randomize-btn":
            self.randomize_stats()
        
        # Fervor buttons
        elif button_id == "fervor-minus":
            if self.character.divine_fervor > 1:
                self.character.divine_fervor -= 1
                self.update_fervor_display()
        
        elif button_id == "fervor-plus":
            if self.character.divine_fervor < 10:
                self.character.divine_fervor += 1
                self.update_fervor_display()
        
        elif button_id == "fervor-min":
            self.character.divine_fervor = 1
            self.update_fervor_display()
        
        elif button_id == "fervor-max":
            self.character.divine_fervor = 10
            self.update_fervor_display()
        
        # Navigation buttons
        elif button_id == "cancel-btn":
            self.action_cancel()
        
        elif button_id == "confirm-btn":
            self.confirm_character()
    
    def randomize_stats(self) -> None:
        """Generate random stats within point-buy constraints"""
        # Simple randomization: distribute 27 points randomly
        stats = ["strength", "dexterity", "constitution", 
                "intelligence", "wisdom", "charisma"]
        
        # Reset to base
        for stat in stats:
            setattr(self.character, stat, 8)
        
        # Randomly distribute points
        points_to_spend = 27
        while points_to_spend > 0:
            stat = random.choice(stats)
            if self.character.can_increase_stat(stat):
                current = getattr(self.character, stat)
                cost = self.character._stat_cost(current + 1) - self.character._stat_cost(current)
                if cost <= points_to_spend:
                    setattr(self.character, stat, current + 1)
                    points_to_spend -= cost
            
            # Prevent infinite loops
            if all(getattr(self.character, s) >= 15 for s in stats):
                break
        
        self.update_all_stat_displays()
        self.notify("Stats randomized!", severity="information")
    
    def on_input_changed(self, event: Input.Changed) -> None:
        """Update character name as user types"""
        if event.input.id == "name-input":
            self.character.name = event.value.strip()
    
    def on_tabbed_content_tab_activated(self, event: TabbedContent.TabActivated) -> None:
        """Update review tab when it's activated"""
        if event.pane.id == "review-tab":
            self.update_review()
    
    def confirm_character(self) -> None:
        """Validate and confirm character creation"""
        if not self.character.name:
            self.notify("Please enter a name!", severity="warning")
            # Switch to name tab
            self.query_one(TabbedContent).active = "name-tab"
            return
        
        if self.character.points_remaining != 0:
            self.notify(
                f"You must spend all points! {self.character.points_remaining} remaining.",
                severity="warning"
            )
            # Switch to attributes tab
            self.query_one(TabbedContent).active = "attr-tab"
            return
        
        # TODO: Save character and transition to game
        self.notify(
            f"Character created: {self.character.name}! (Game view coming soon...)",
            severity="information"
        )
    
    def action_cancel(self) -> None:
        """Return to main menu"""
        self.app.pop_screen()
    
    def action_next_tab(self) -> None:
        """Navigate to next tab"""
        tabs = self.query_one(TabbedContent)
        # Textual handles tab cycling automatically with focus
        
    def action_prev_tab(self) -> None:
        """Navigate to previous tab"""
        tabs = self.query_one(TabbedContent)
        # Textual handles tab cycling automatically with focus