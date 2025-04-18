from Board import Board
from Minmax import Minmax
import time
class Game:
    def __init__(self):
        self.ai_symbol='X'
        self.human_symbol='O'
        self.board = Board()
        self.ai = Minmax(self.ai_symbol,  self.human_symbol)
        self.current_player =  self.human_symbol 

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def get_user_move(self):
        while True:
            try:
                x = int(input("Enter row (0-2): "))
                y = int(input("Enter col (0-2): "))
                if 0 <= x < 3 and 0 <= y < 3 and self.board.is_cell_empty(x, y):
                    return x, y
                print("Invalid move. Try again.")
            except ValueError:
                print("Please enter numbers only.")

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.print_board()
        while True:
            if self.current_player ==  self.human_symbol:
                print("\nYour turn:")
                x, y = self.get_user_move()
                self.board.set_cell(x, y,  self.human_symbol)
            else:
                print("\nAI is making a move...")
                x, y = self.ai.get_best_move(self.board)
                self.board.set_cell(x, y,  self.ai_symbol)
                time.sleep(1)
            self.board.print_board()
            score = self.board.evluate( self.ai_symbol,  self.human_symbol)
            if score == 10:
                print("AI wins!")
                break
            elif score == -10:
                print("You win!")
                break
            elif self.board.is_full():
                print("It's a draw!")
                break
            self.switch_player()


game=Game()
game.play()