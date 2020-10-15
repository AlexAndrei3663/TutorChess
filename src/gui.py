import tkinter as tk
from chessGame.boardgame import Board

def main(Board):
    root = tk.Tk()
    root.title("Chess")
    #gui.draw_board()
    #gui.draw_pieces()
    root.mainloop()

if __name__ == "__main__":
    game = Board
    main(game)


