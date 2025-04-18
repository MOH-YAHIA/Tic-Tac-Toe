import tkinter as tk
from tkinter import messagebox
from Board import Board
from Minmax import Minmax

class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe - AI")
        self.board = Board()
        self.ai = Minmax('X', 'O')
        self.current_player = 'O'
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(3):
            for j in range(3):
                btn = tk.Button(frame, text=' ', font=('Helvetica', 32), width=5, height=2,
                                command=lambda x=i, y=j: self.on_click(x, y))
                btn.grid(row=i, column=j)
                self.buttons[i][j] = btn

        restart_btn = tk.Button(self.root, text="Restart", font=('Helvetica', 14), command=self.reset_game)
        restart_btn.pack(pady=10)

    def on_click(self, x, y):
        if self.board.is_cell_empty(x, y) and self.current_player == 'O':
            self.board.set_cell(x, y, 'O')
            self.buttons[x][y].config(text='O', state='disabled')
            self.check_game_end()
            self.current_player = 'X'
            self.root.after(500, self.ai_move)  

    def ai_move(self):
        if self.current_player == 'X':
            x, y = self.ai.get_best_move(self.board)
            if x != -1 and y != -1:
                self.board.set_cell(x, y, 'X')
                self.buttons[x][y].config(text='X', state='disabled')
            self.check_game_end()
            self.current_player = 'O'

    def check_game_end(self):
        score = self.board.evluate('X', 'O')
        if score == 10:
            self.show_result("AI wins!")
        elif score == -10:
            self.show_result("You win!")
        elif self.board.is_full():
            self.show_result("It's a draw!")

    def show_result(self, message):
        messagebox.showinfo("Game Over", message)
        self.disable_all_buttons()

    def disable_all_buttons(self):
        for row in self.buttons:
            for btn in row:
                btn.config(state='disabled')

    def reset_game(self):
        self.board = Board()
        self.current_player = 'O'
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ', state='normal')

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
