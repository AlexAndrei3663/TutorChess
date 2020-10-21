import tkinter as tk
from chessGame.boardgame import Board


class GUI:
    pieces = {}
    selected_piece = None
    focused = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor = "khaki"
    rows = 8
    columns = 8
    dim_square = 64

    def __init__(self, parent, chessboard):
        self.chessboard = chessboard
        self.parent = parent
        # Adding Top Menu
        self.menubar = tk.Menu(parent)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Novo Jogo", command=self.new_game)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        # Adding Frame
        self.btmfrm = tk.Frame(parent, height=64)
        self.info_label = tk.Label(self.btmfrm,
                                text="   Peças brancas para começar  ",
                                fg=self.color2)
        self.info_label.pack(side=tk.RIGHT, padx=8, pady=5)
        self.btmfrm.pack(fill="x", side=tk.BOTTOM)

        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = tk.Canvas(parent, width=canvas_width,
                               height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.draw_board()
        #self.canvas.bind("<Button-1>", self.square_clicked)

    def new_game(self):
        #self.chessboard.show(chessboard.START_PATTERN)
        self.draw_board()
        #self.draw_pieces()
        self.info_label.config(text="   Peças brancas para começar  ", fg='red')

    def draw_board(self):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square)
                y1 = ((7 - row) * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if (self.focused is not None and (row, col) in self.focused):
                    self.canvas.create_rectangle(x1, y1, x2, y2,
                                                 fill=self.highlightcolor,
                                                 tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color,
                                                 tags="area")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.pieces[name] = (self.pieces[name][0], self.pieces[name][1])
            x0 = (self.pieces[name][1] * self.dim_square) + int(
                self.dim_square / 2)
            y0 = ((7 - self.pieces[name][0]) * self.dim_square) + int(
                self.dim_square / 2)
            self.canvas.coords(name, x0, y0)
        self.canvas.tag_raise("Ocupado")
        self.canvas.tag_lower("area")

def main(Board):
    root = tk.Tk()
    root.title("Tutor Chess")
    gui = GUI(root, Board)
    gui.draw_board()
    #gui.draw_pieces()
    root.mainloop()

if __name__ == "__main__":
    game = Board
    main(game)


