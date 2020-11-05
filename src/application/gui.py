import tkinter as tk
from .UI import UI
from chessGame.boardgame.Position import Position
from chessGame.chess import ChessException, ChessMatch
from chessGame.chess.ChessPosition import ChessPosition
from stockfish import Stockfish

class GUI:
    pieces = {}
    focused = None
    source = None
    images = {}
    color1 = "#DDB88C"
    color2 = "#A66D4F"
    highlightcolor = "khaki"
    rows = 8
    columns = 8
    dim_square = 64

    def __init__(self, chess_match, stockfish): 
        self.__chess_match = chess_match
        self.__stockfish = stockfish
        self.parent = tk.Tk()
        self.parent.title("Tutor Chess")

        # Adding Top Menu
        self.menubar = tk.Menu(self.parent)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="Novo Jogo", command=self.new_game)
        self.menubar.add_cascade(label="Menu", menu=self.filemenu)
        self.parent.config(menu=self.menubar)

        # Adding Frame
        self.btmfrm = tk.Frame(self.parent, height=64)
        self.info_label = tk.Label(self.btmfrm, text="  Peças brancas para começar  ", fg=self.color2)
        self.info_label.pack(side=tk.RIGHT, padx=8, pady=5)
        self.btmfrm.pack(fill="x", side=tk.BOTTOM)

        canvas_width = self.columns * self.dim_square
        canvas_height = self.rows * self.dim_square
        self.canvas = tk.Canvas(self.parent, width=canvas_width, height=canvas_height)
        self.canvas.pack(padx=8, pady=8)
        self.canvas.bind("<Button-1>", self.square_clicked)

    def new_game(self):
        #self.chessboard.show(chessboard.START_PATTERN)
        self.draw_board()
        self.draw_pieces()
        self.info_label.config(text="   Peças brancas para começar  ", fg='red')

    def square_clicked(self, event):
        col_size = row_size = self.dim_square
        if not self.source:
            try:
                self.source = ChessPosition._from_position(Position(int(event.y / row_size), int(event.x / col_size)))
                self.focused = self.__chess_match.possible_move(self.source)
                self.draw_board()
            except ChessException.ChessException as e:
                self.source = None
                print(e)
        else:
            try:
                target = ChessPosition._from_position(Position(int(event.y / row_size), int(event.x / col_size)))
                captured_piece = self.__chess_match.perform_chess_move(self.source, target)
            except ChessException.ChessException as e:
                print(e)

            self.source = None
            self.focused = None
            self.__stockfish.set_fen_position(self.__chess_match.get_fen_notation())
            if self.__chess_match.current_player == 'BLACK':
                moviment = self.__stockfish.get_best_move()
                captured_piece = self.__chess_match.perform_chess_move(
                    ChessPosition(moviment[0], int(moviment[1])), 
                    ChessPosition(moviment[2], int(moviment[3]))
                )
            self.draw_board()
            self.draw_pieces()
        if self.__chess_match.checkmate or self.__chess_match.draw:
            self.parent.quit()
            
    def draw_board(self):
        color = self.color2
        for row in range(self.rows):
            color = self.color1 if color == self.color2 else self.color2
            for col in range(self.columns):
                x1 = (col * self.dim_square)
                y1 = (row * self.dim_square)
                x2 = x1 + self.dim_square
                y2 = y1 + self.dim_square
                if (self.focused is not None and self.focused[row][col]):
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.highlightcolor, tags="area")
                else:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, tags="area")
                color = self.color1 if color == self.color2 else self.color2
        for name in self.pieces:
            self.pieces[name] = (self.pieces[name][0], self.pieces[name][1])
            x0 = (self.pieces[name][1] * self.dim_square) + int(self.dim_square / 2)
            y0 = ((7 - self.pieces[name][0]) * self.dim_square) + int(self.dim_square / 2)
            self.canvas.coords(name, x0, y0)
        self.canvas.tag_raise("Ocupado")
        self.canvas.tag_lower("area")

    def draw_pieces(self):
        self.canvas.delete("Ocupado")
        pieces = self.__chess_match.pieces()
        for i in range(len(pieces)):
            for j in range(len(pieces)):
                piece = pieces[i][j]
                if piece:
                    filename = "./src/pieces_image/%s%s.png" % (str(piece).lower(), piece.color.lower())
                    piecename = "%s%s%s" % (str(piece), i, j)
                    if filename not in self.images:
                        self.images[filename] = tk.PhotoImage(file=filename)
                    self.canvas.create_image(0, 0, image=self.images[filename], tags=(piecename, "Ocupado"), anchor="c")
                    x0 = (j * self.dim_square) + int(self.dim_square / 2)
                    y0 = (i * self.dim_square) + int(self.dim_square / 2)
                    self.canvas.coords(piecename, x0, y0)