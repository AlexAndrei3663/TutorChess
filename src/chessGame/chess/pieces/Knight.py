from .. import ChessPiece
from chessGame.boardgame.Position import Position
from estruturasDeDados import ListaDuplamenteEncadeada as Lista
import copy

class Knight(ChessPiece.ChessPiece):

    def __init__(self, board, color):
        super().__init__(board, color)
        self.__value = 320
        self.__square_table = [
            [-50,-40,-30,-30,-30,-30,-40,-50],
            [-40,-20,  0,  0,  0,  0,-20,-40],
            [-30,  0, 10, 15, 15, 10,  0,-30],
            [-30,  5, 15, 20, 20, 15,  5,-30],
            [-30,  0, 15, 20, 20, 15,  0,-30],
            [-30,  5, 10, 15, 15, 10,  5,-30],
            [-40,-20,  0,  5,  5,  0,-20,-40],
            [-50,-40,-30,-30,-30,-30,-40,-50]
        ]

    # Sobrecarga toString
    def __str__(self):
        return 'n' if self.color == 'BLACK' else 'N'

    # Checa se é possível se movimentar
    def __can_move(self, position):
        p = self.board.piece(position.row, position.column)
        return p == None or p.color != self.color

    # Sobrecarga get_evaluation
    def get_evaluation(self, position):
        return self.__square_table[position.row if self.color == 'WHITE' else 7 - position.row][position.column] + self.__value

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = Lista.Lista(8, copy.copy(Lista.Lista(8, False)))

        # Movimentos pra cima/direita
        p = Position(self._position.row - 2, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra direita/cima
        p = Position(self._position.row - 1, self._position.column + 2)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra direita/baixo
        p = Position(self._position.row + 1, self._position.column + 2)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra baixo/direita
        p = Position(self._position.row + 2, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra baixo/esquerda
        p = Position(self._position.row + 2, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra esquerda/baixo
        p = Position(self._position.row + 1, self._position.column - 2)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra esquerda/cima
        p = Position(self._position.row - 1, self._position.column - 2)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra cima/esquerda
        p = Position(self._position.row - 2, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        return mat