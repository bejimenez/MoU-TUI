# Ulan - Realm of 1001 Gods
## A Terminal-Based RPG Adventure

### Project Overview
A text-based RPG (TUI) set in the world of Ulan, where 1001 powerful beings known as "gods" rule over mortal realms. These gods are not true deities - they can be killed, and each death weakens the remaining gods. To preserve their power, the gods wage their conflicts through mortal proxies, creating a world of intrigue, heroism, and divine manipulation.

**Technology Stack:**
- Python 3.x
- Textual (TUI framework)
- Rich (text formatting, bundled with Textual)

---

## Setup Instructions

### Initial Setup
1. **Clone the repository:**
   ```bash
   git clone <https://github.com/bejimenez/MoU-TUI>
   cd MoU-TUI
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Linux/Mac:** `source venv/bin/activate`
   - **Windows:** `venv\Scripts\activate`

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the game:**
   ```bash
   python main.py
   ```

---

## Project Structure

```
ulan-rpg/
├── README.md              # This file
├── requirements.txt       # Python dependencies
├── main.py               # Entry point for the game
├── src/                  # Source code directory
│   ├── game/            # Game logic and engine
│   │   └── character.py # Character data structures
│   ├── ui/              # User interface components
│   │   └── screens/     # UI screens
│   │       ├── main_menu.py          # Main menu screen
│   │       └── character_creation.py # Character creation screen
│   └── world/           # World data and lore
└── tests/               # Unit tests
```

---

## Current Features

### Implemented
- [x] Basic Textual app structure
- [x] Main menu screen
- [x] Tabbed character creation interface
  - Name input
  - Attribute allocation (D&D point-buy system)
  - Divine Fervor slider (1-10 scale)
  - Character review tab
- [x] Character data model with loyalty system foundation

### In Progress
- [ ] Game view screen (next step)
- [ ] Save/Load system
- [ ] Loyalty mechanics implementation

### Not Yet Started
- [ ] Combat system
- [ ] Inventory management
- [ ] World exploration

---

## Game Systems

### Character Stats
**Traditional D&D Attributes:**
- Strength, Dexterity, Constitution, Intelligence, Wisdom, Charisma
- Point-buy system: 27 points total, stats range 8-15
- Higher values cost more points (13→14 costs 2, 14→15 costs 2)

### Divine Fervor System (Unique to Ulan)
**What is Divine Fervor?**
Divine Fervor represents a character's natural tendency toward zealotry and devotion. It's a psychological trait set at character creation that determines how quickly they gain loyalty with gods.

**Scale:** 1-10
- **Low Fervor (1-3):** Pragmatic Soul
  - Slow loyalty gain
  - Can serve multiple gods more easily
  - Flexible but less powerful god-specific bonuses
  
- **Medium Fervor (4-7):** Balanced Devotion
  - Moderate loyalty gain
  - Versatile approach
  
- **High Fervor (8-10):** Zealous Heart
  - Rapid loyalty gain
  - Becomes locked into fewer gods
  - Powerful god-specific bonuses but less flexibility

### Loyalty System (Foundation Laid, Not Yet Implemented)
**Concept:**
- Each character starts at 0 (neutral) loyalty with all gods
- Loyalty increases through quests, offerings, and actions aligned with a god's domain
- Loyalty gain rate: `base_gain * (divine_fervor / 5)`
- High loyalty unlocks god-specific perks, items, and story branches
- Multiple high-loyalty relationships create conflicts and penalties

**Strategic Implications:**
- Replaces traditional class system with emergent gameplay
- High Fervor = powerful specialist build (like a Paladin)
- Low Fervor = flexible generalist build (diplomatic character)
- Antagonist gods can be served simultaneously for unique synergies

---

## World of Ulan - Quick Reference

### Core Concepts
- **The 1001 Gods:** Powerful beings considered deities, but mortal
- **Divine Weakening:** When a god dies, all remaining gods lose power
- **Proxy Wars:** Gods use mortal champions to fight their battles
- **God Champions:** Mortals who have gained the favor of a particular god(s) and have earned immense power

### Key Themes
- Divine politics and manipulation
- Mortal agency vs. divine will
- The price of power
- Myths vs. reality

---

## Development Notes

### Design Principles
1. **Keep functions short:** Max 60 lines per function
2. **Minimal dependencies:** Only add packages when truly necessary
3. **Simple first:** Add complexity only when needed
4. **Document as you go:** Update this README each session

### Code Standards
- Use type hints where practical
- Write docstrings for non-obvious functions
- Keep UI separate from game logic
- Make components modular and testable

---

## Where I Left Off

**Last Session Date:** January 17, 2026

**What I Was Working On:**
Implemented tabbed character creation screen with Divine Fervor system

**What Works:**
- Main menu navigation
- Complete character creation flow:
  - Tab 1: Name input
  - Tab 2: Attribute allocation (point-buy with randomize button)
  - Tab 3: Divine Fervor selection
  - Tab 4: Character review and validation
- Character data model with point-buy validation
- All UI properly styled with gold/cyan theme

**What's Broken/Incomplete:**
- Character data is created but not saved (no persistence yet)
- No game view screen yet (clicking "Begin Journey" shows notification)
- Loyalty mechanics defined conceptually but not implemented

**Next Steps:**
1. Create basic game view screen to transition into after character creation
2. Implement character persistence (save/load)
3. Add basic world/location system
4. Begin implementing loyalty gain mechanics during gameplay

**Questions/Ideas:**
- Should we add a biography/backstory field during character creation for roleplay flavor?
- Consider adding stat modifiers display (show bonuses based on stat values)
- Think about how to visualize loyalty levels in the UI (progress bars? relationship web?)

---

## Character Creation - Technical Details

### Point-Buy Cost Calculation
```python
Base stat: 8 (costs 0 points)
9-13: 1 point per increase
14: 2 points (total 7 points from base)
15: 2 points (total 9 points from base)
```

### Divine Fervor Flavor Text
- **1-3:** "You approach the gods with caution. Loyalty builds slowly, but you remain free to serve many masters."
- **4-6:** "You walk the middle path. Neither fanatic nor skeptic, you can adapt as needed."
- **7-10:** "Faith burns bright within you. Your devotion grows swiftly, but you struggle to serve conflicting gods."

### Character Data Structure
```python
@dataclass
class Character:
    name: str
    strength: int  # 8-15
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    divine_fervor: int  # 1-10
    loyalty: dict[str, int]  # {god_name: loyalty_value}
```

---

## Quick Start Guide (For Future Me)

When returning to this project after time away:

1. **Read the "Where I Left Off" section above** ⬆️
2. **Activate the virtual environment:** `source venv/bin/activate` (or Windows equivalent)
3. **Run the current build:** `python main.py`
4. **Test character creation:** Click "New Game" and go through all tabs
5. **Review the last few git commits:** `git log --oneline -5`
6. **Check for TODOs in code:** `grep -r "TODO" src/`

---

## Resources & References

### Textual Documentation
- [Official Textual Docs](https://textual.textualize.io/)
- [Textual Widget Gallery](https://textual.textualize.io/widget_gallery/)

### World Building Notes
*(To be expanded as the world develops)*