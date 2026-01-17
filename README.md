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
│   ├── ui/              # User interface components
│   └── world/           # World data and lore
└── tests/               # Unit tests
```

---

## Current Features

### Implemented
- [x] Basic Textual app structure
- [x] Main menu screen
- [ ] Character creation
- [ ] Combat system
- [ ] Inventory management
- [ ] Save/Load system

### In Progress
Update the character creation screen with tabs to prepare for more interesting mechanics

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

**Last Session Date:** *[Update this each time you work on the project]*

**What I Was Working On:**
building the character creation system

**What Works:**


**What's Broken/Incomplete:**


**Next Steps:**
- continue character creation screen with tabs for assigning attributes and picking background. 

**Questions/Ideas:**
maybe implement a biography section for flavor? (need to consider how to use it in game...)

---

## Quick Start Guide (For Future Me)

When returning to this project after time away:

1. **Read the "Where I Left Off" section above** ⬆️
2. **Activate the virtual environment:** `source venv/bin/activate` (or Windows equivalent)
3. **Run the current build:** `python main.py`
4. **Review the last few git commits:** `git log --oneline -5`
5. **Check for TODOs in code:** `grep -r "TODO" src/`

---

## Resources & References

### Textual Documentation
- [Official Textual Docs](https://textual.textualize.io/)
- [Textual Widget Gallery](https://textual.textualize.io/widget_gallery/)

### World Building Notes
