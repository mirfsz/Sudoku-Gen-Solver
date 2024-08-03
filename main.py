import tkinter as tk
from tkinter import messagebox
import random
import copy

class SudokuSolver:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Solver")
        self.cells = {}
        self.create_grid()
        self.create_buttons()
        self.selected_cell = None

    def create_grid(self):
        container = tk.Frame(self.master, bd=1, relief=tk.SUNKEN)
        container.grid(row=0, column=0, padx=5, pady=5)

        for row in range(9):
            for col in range(9):
                cell = tk.Entry(container, width=2, font=('Arial', 18), justify='center')
                cell.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
                cell.insert(0, "")
                cell.bind("<FocusIn>", self.cell_focused)
                cell.bind("<KeyRelease>", self.key_pressed)
                self.cells[(row, col)] = cell

                if (row in [0, 1, 2, 6, 7, 8] and col in [3, 4, 5]) or \
                   (row in [3, 4, 5] and col in [0, 1, 2, 6, 7, 8]):
                    cell.config(bg='lightgray')

    def create_buttons(self):
        button_frame = tk.Frame(self.master)
        button_frame.grid(row=1, column=0, pady=10)

        solve_button = tk.Button(button_frame, text="Solve", command=self.solve)
        solve_button.grid(row=0, column=0, padx=5)

        clear_button = tk.Button(button_frame, text="Clear", command=self.clear)
        clear_button.grid(row=0, column=1, padx=5)

        generate_button = tk.Button(button_frame, text="Generate Puzzle", command=self.generate_puzzle)
        generate_button.grid(row=0, column=2, padx=5)

    def cell_focused(self, event):
        self.selected_cell = event.widget

    def key_pressed(self, event):
        if self.selected_cell:
            value = self.selected_cell.get()
            if value and value[-1] in "123456789":
                self.selected_cell.delete(0, tk.END)
                self.selected_cell.insert(0, value[-1])
            elif value and value[-1] not in "123456789":
                self.selected_cell.delete(0, tk.END)
            self.highlight_conflicts()

    def get_board(self):
        board = []
        for row in range(9):
            board_row = []
            for col in range(9):
                val = self.cells[(row, col)].get()
                board_row.append(int(val) if val.isdigit() else 0)
            board.append(board_row)
        return board

    def set_board(self, board):
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                self.cells[(row, col)].delete(0, tk.END)
                self.cells[(row, col)].insert(0, str(val) if val != 0 else "")
        self.highlight_conflicts()

    def solve(self):
        board = self.get_board()
        if self.solve_sudoku(board):
            self.set_board(board)
        else:
            messagebox.showerror("Error", "No solution exists for this Sudoku puzzle.")

    def solve_sudoku(self, board):
        empty = self.find_empty(board)
        if not empty:
            return True
        row, col = empty

        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                self.cells[(row, col)].delete(0, tk.END)
                self.cells[(row, col)].insert(0, str(num))
                self.master.update()
                self.master.after(10)  # Delay for visualization

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0
                self.cells[(row, col)].delete(0, tk.END)
                self.master.update()

        return False

    def find_empty(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return (row, col)
        return None

    def is_valid(self, board, num, pos):
        for col in range(9):
            if board[pos[0]][col] == num and pos[1] != col:
                return False

        for row in range(9):
            if board[row][pos[1]] == num and pos[0] != row:
                return False

        box_x, box_y = pos[1] // 3, pos[0] // 3
        for row in range(box_y * 3, box_y * 3 + 3):
            for col in range(box_x * 3, box_x * 3 + 3):
                if board[row][col] == num and (row, col) != pos:
                    return False

        return True

    def clear(self):
        for cell in self.cells.values():
            cell.delete(0, tk.END)
            cell.config(fg='black')

    def highlight_conflicts(self):
        board = self.get_board()
        for row in range(9):
            for col in range(9):
                if board[row][col] != 0:
                    temp = board[row][col]
                    board[row][col] = 0
                    if not self.is_valid(board, temp, (row, col)):
                        self.cells[(row, col)].config(fg='red')
                    else:
                        self.cells[(row, col)].config(fg='black')
                    board[row][col] = temp

    def generate_puzzle(self):
        self.clear()
        board = self.generate_solved_board()
        self.remove_numbers(board)
        self.set_board(board)

    def generate_solved_board(self):
        board = [[0 for _ in range(9)] for _ in range(9)]
        self.fill_board(board)
        return board

    def fill_board(self, board):
        numbers = list(range(1, 10))
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    random.shuffle(numbers)
                    for num in numbers:
                        if self.is_valid(board, num, (row, col)):
                            board[row][col] = num
                            if self.fill_board(board):
                                return True
                            board[row][col] = 0
                    return False
        return True

    def remove_numbers(self, board):
        cells = [(row, col) for row in range(9) for col in range(9)]
        random.shuffle(cells)
        removed = 0
        for cell in cells:
            if removed >= 40:  # Adjust this number to control difficulty
                break
            row, col = cell
            temp = board[row][col]
            board[row][col] = 0
            copy_board = copy.deepcopy(board)
            if self.count_solutions(copy_board) == 1:
                removed += 1
            else:
                board[row][col] = temp

    def count_solutions(self, board):
        empty = self.find_empty(board)
        if not empty:
            return 1
        row, col = empty
        count = 0
        for num in range(1, 10):
            if self.is_valid(board, num, (row, col)):
                board[row][col] = num
                count += self.count_solutions(board)
                if count > 1:
                    return 2
                board[row][col] = 0
        return count

if __name__ == "__main__":
    root = tk.Tk()
    SudokuSolver(root)
    root.mainloop()