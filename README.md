# Duck n Dodge

Duck n Dodge is a single-player dodge game set in the hottest nightclub, Club Velocity. A fight breaks out, and bottles are hurled across the room. Dodge the bottles for 45 seconds to win. The game is a lighthearted take on a familiar nightlife scenario — the moment when things go left.

## Overview

Duck n Dodge is meant to be a quick, replayable arcade game. It's a reflex test dressed up in a nightlife theme. The goal is simple — dodge the bottles - make it out to dance again.

Players start on the title screen and advance to a directions screen. Pressing any key starts gameplay. The player (blue square) is centered in the room while bottles (red) approach from both sides. The player has 45 seconds to avoid being struck. If they last the entire 45 seconds, they win.

**Main features:**

- Single-player
- Bottles fall from both directions at random speeds
- Flashing club lighting
- 45-second countdown timer
- Title, directions, game-over, and win screens
- Option to replay

## Prerequisites

- **Python 3** — the game runs on Python 3.
- **pygame** — for the game window, drawing, input handling, and the game loop.
- A terminal (Command Prompt, Terminal, or similar) to install dependencies and launch the game.
- A display — the game opens a window, so it needs a screen.

## Installation Instructions

1. **Confirm Python 3 is installed.**
   Open your terminal and type:
   ```
   python3 --version
   ```
   If it prints `Python 3.x.x`, you're good. If not, download Python 3 from [python.org](https://www.python.org/).

2. **Get the project files.**
   Choose one of these options:

   - **Clone the repository (recommended if you have Git).**
     Open your terminal and type:
     ```
     git clone https://github.com/randycreates/duckndodge.git
     cd duckndodge
     ```

   - **Download the ZIP.**
     Click the green **Code** button on the repository page, then select **Download ZIP**. Unzip the file into a folder of your choice.

3. **Install dependencies.**
   In your terminal, type:
   ```
   pip install pygame
   ```

**Platform Notes**

- **Windows:** Paths use backslashes (`\`) instead of forward slashes (`/`). The `cd` command works the same way.
- **macOS and Linux:** The instructions work as written.

## How to Run the Program

1. Open your terminal.
2. Navigate to the folder containing `duckndodge.py`:
   ```
   cd path/to/your/folder
   ```
3. Run the game:
   ```
   python3 duckndodge.py
   ```
4. A game window will open on your screen.

## Usage Instructions

When the game launches, you'll see the title screen for **Club Velocity**. Press any key to continue.

The next screen explains the game. Press any key to start the round.

**During gameplay:**

- Use the **left and right arrow keys** to move the player (the blue square) across the screen.
- Bottles (red squares) fall from the top and bottom at random speeds. Avoid them.
- A countdown timer in the top-left corner shows how many seconds remain.
- If a bottle hits you, the round ends.
- If you survive the full 45 seconds, you win.

**After the round:**

- On the game-over screen or the win screen, press **Y** to play again.
- Press **Escape** during gameplay to quit.

## Known Limitations

- **Single-player only.** The game does not support multiplayer or score tracking.
- **No audio.** The current version runs silently. An original soundtrack exists but is not included in this repository.
- **Fixed difficulty.** The number of bottles is randomized at the start of each wave and the speed varies. 
- **No save state.** Closing the window ends the session. There's no progress to save.

## License

This project is not licensed. All rights reserved. The game code and any included assets are the original work of Randy Jones Jr.

## Acknowledgements

- **Pygame** — the game library used to build Duck n Dodge. The [Pygame beginner's guide](https://www.pygame.org/docs/tut/newbieguide.html) was a helpful reference.
- **Python** — the language the game is written in.
- **DeepSeek** — used for concept explanations, step-by-step guidance, debugging support, and code review throughout development.

