# Sudoku Solver

A Python-based Sudoku solver with a graphical user interface using Tkinter.

## Features

- Interactive 9x9 Sudoku grid
- Solve button to automatically solve the puzzle
- Clear button to reset the board
- Generate Puzzle button to create a new Sudoku puzzle
- Real-time conflict highlighting
- Visual solving process

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository or download the `sudoku_solver.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script using Python:
python sudoku_solver.py

## How to Use

1. Input numbers manually into the cells or use the "Generate Puzzle" button to create a new puzzle.
2. Click "Solve" to solve the puzzle automatically.
3. Use "Clear" to reset the board.
4. Red numbers indicate conflicts with Sudoku rules.

## Code Structure

- `SudokuSolver` class: Main class containing all the game logic and GUI elements.
- `create_grid()`: Sets up the 9x9 grid of entry widgets.
- `create_buttons()`: Adds functional buttons to the interface.
- `solve_sudoku()`: Implements the backtracking algorithm to solve the puzzle.
- `generate_puzzle()`: Creates a new, valid Sudoku puzzle.
- `highlight_conflicts()`: Checks and highlights conflicting numbers.

## To-Do List for Improvements

1. Add difficulty levels for puzzle generation (Easy, Medium, Hard).
2. Implement a timer to track solving time.
3. Add an option to save and load puzzles.
4. Create a hint system to help users solve puzzles.
5. Improve the GUI design for a more polished look.
6. Add keyboard shortcuts for common actions.
7. Implement an undo/redo feature.
8. Add a feature to check if the current state of the puzzle is solvable.
9. Create a scoring system based on solving time and difficulty.
10. Add animations for the solving process to make it more visually appealing.
11. Implement a pencil mark feature for noting possible numbers in cells.
12. Add sound effects for interactions and puzzle completion.
13. Create a dark mode option for the interface.
14. Implement localization to support multiple languages.
15. Add an option to print puzzles.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).
