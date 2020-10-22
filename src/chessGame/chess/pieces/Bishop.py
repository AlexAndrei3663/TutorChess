from .. import ChessPiece
from chessGame.boardgame.Position import Position
from estruturasDeDados import ListaDuplamenteEncadeada as Lista
import copy

class Bishop(ChessPiece.ChessPiece):

    def __init__(self, board, color):
        super().__init__(board, color)
        self.__value = 330
        self.__square_table = [
            [-20,-10,-10,-10,-10,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5, 10, 10,  5,  0,-10],
            [-10,  5,  5, 10, 10,  5,  5,-10],
            [-10,  0, 10, 10, 10, 10,  0,-10],
            [-10, 10, 10, 10, 10, 10, 10,-10],
            [-10,  5,  0,  0,  0,  0,  5,-10],
            [-20,-10,-10,-10,-10,-10,-10,-20]
        ]

    # Sobrecarga toString
    def __str__(self):
        return 'b' if self.color == 'BLACK' else 'B'

    # Sobrecarga get_evaluation
    def get_evaluation(self, position):
        return self.__square_table[position.row if self.color == 'WHITE' else 7 - position.row][position.column] + self.__value

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = Lista.Lista(8, copy.copy(Lista.Lista(8, False)))

        # Movimentos pra cima/direita
        p = Position(self._position.row - 1, self._position.column + 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row - 1, p.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra cima/esquerda
        p = Position(self._position.row - 1, self._position.column - 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row - 1, p.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/direita
        p = Position(self._position.row + 1, self._position.column + 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row + 1, p.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/esquerda
        p = Position(self._position.row + 1, self._position.column - 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row + 1, p.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        return mat