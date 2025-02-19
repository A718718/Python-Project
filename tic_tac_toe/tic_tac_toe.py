import tkinter as tk
from tkinter import messagebox
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False

        # Create buttons
        self.buttons = []
        for i in range(9):
            button = tk.Button(root, text="", font=('Helvetica', 20), height=3, width=6,
                               bg='lightblue', command=lambda i=i: self.make_move(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

        # Reset button
        self.reset_button = tk.Button(root, text="Reset Game", font=('Helvetica', 12),
                                      command=self.reset_game, bg='orange', fg='white')
        self.reset_button.grid(row=3, column=0, columnspan=3, sticky="we")

    def make_move(self, position):
        if not self.game_over and self.board[position] == "":
            self.board[position] = self.current_player
            self.buttons[position].config(text=self.current_player, fg='black')

            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "":
                self.highlight_winner(i, i + 1, i + 2)
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                self.highlight_winner(i, i + 3, i + 6)
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            self.highlight_winner(0, 4, 8)
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            self.highlight_winner(2, 4, 6)
            return True

        return False

    def highlight_winner(self, a, b, c):
        self.buttons[a].config(bg='green')
        self.buttons[b].config(bg='green')
        self.buttons[c].config(bg='green')

    def reset_game(self):
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        for button in self.buttons:
            button.config(text="", bg='lightblue')


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()