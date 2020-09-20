import Board
import ChessPosition
import Rook
import King

# Tabuleiro visível ao jogador
class ChessMatch:

    def __init__(self):
        self.__board = Board.Board(8, 8)
        self.initial_setup()

    # Retorna a matriz com as peças
    def pieces(self):
        # mat = [[None]*self.__board.columns]*self.__board.rows
        mat = []

        for i in range(self.__board.columns):
            row = []
            for j in range(self.__board.columns):
                row.append(self.__board.piece(i, j))
                # mat[i][j] = self.__board.piece(i, j)
            mat.append(row)
        return mat

    # Setup inicial do tabuleiro
    def initial_setup(self):
        self.__place_new_piece('a', 1, Rook.Rook(self.__board, True))
        self.__place_new_piece('f', 5, King.King(self.__board, False))

    # Função para posicionar nova peça ja convertendo char/int pra int/int
    def __place_new_piece(self, column, row, piece):
        self.__board.place_piece(piece, ChessPosition.ChessPosition(column, row)._to_position())