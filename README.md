# Minesweeper Game

This is a simple implementation of the classic Minesweeper game using Pygame.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Features](#features)
- [Controls](#controls)

## Installation

### Prerequisites
- Python 3.x
- Pygame library

### Steps
1. Clone the repository:
    ```sh
    git clone https://github.com/AkshithaKola/Minesweeper.git
    cd minesweeper
    ```
2. Install Pygame:
    ```sh
    pip install pygame
    ```
3. Ensure you have `mine.png` and `flag.png` in the same directory as your script.

## Usage

1. Run the script:
    ```sh
    python minesweeper.py
    ```

2. The game window will open with a 10x10 grid.

3. Use the mouse to interact with the game.

## Game Rules

- The goal of the game is to uncover all the cells that do not contain mines.
- The number on a revealed cell indicates how many mines are adjacent to that cell.
- If you reveal a mine, you lose the game.
- Right-click to place a flag on a cell you suspect contains a mine.

## Features

- **Grid Size**: 10x10
- **Number of Mines**: 10
- **Graphics**: Custom images for mines and flags
- **End Game**: Displays a "You lost!" message if you hit a mine and "You won!" message if you uncover all non-mine cells.

## Controls

- **Left Mouse Button**: Reveal a cell
- **Right Mouse Button**: Place/remove a flag
- **Game Over/Win Screen**: 
  - **Replay**: Start the same game again
  - **New Game**: Start a new game with the same settings
  - **Exit**: Quit the game




