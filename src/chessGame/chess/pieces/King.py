from . import Rook
from .. import ChessPiece
from chessGame.boardgame.Position import Position
from estruturasDeDados import ListaDuplamenteEncadeada as Lista
import copy

class King(ChessPiece.ChessPiece):

    def __init__(self, board, color, chess_match):
        super().__init__(board, color)
        self.__chess_match = chess_match
        self.__value = 20000
        self.__square_table = [
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-20,-30,-30,-40,-40,-30,-30,-20],
            [-10,-20,-20,-20,-20,-20,-20,-10],
            [ 20, 20,  0,  0,  0,  0, 20, 20],
            [ 20, 30, 10,  0,  0, 10, 30, 20]
        ]

    # Sobrecarga toString
    def __str__(self):
        return 'k' if self.color == 'BLACK' else 'K'

    # Checa se é possível se movimentar
    def __can_move(self, position):
        p = self.board.piece(position.row, position.column)
        return p == None or p.color != self.color

    # Checa se é possível fazer o rook
    def __test_rook(self, position):
        p = self.board.piece(position.row, position.column)
        return p != None and isinstance(p, Rook.Rook) and p.color == self.color and p.move_count == 0

    # Sobrecarga get_evaluation
    def get_evaluation(self, position):
        return self.__square_table[position.row if self.color == 'WHITE' else 7 - position.row][position.column] + self.__value

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = Lista.Lista(8, copy.copy(Lista.Lista(8, False)))

        # Movimentos pra cima
        p = Position(self._position.row - 1, self._position.column)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra baixo
        p = Position(self._position.row + 1, self._position.column)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra direita
        p = Position(self._position.row, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra esquerda
        p = Position(self._position.row, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra cima/direita
        p = Position(self._position.row - 1, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra cima/esquerda
        p = Position(self._position.row - 1, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra baixo/direita
        p = Position(self._position.row + 1, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimentos pra baixo/esquerda
        p = Position(self._position.row + 1, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat.retorna_elemento(p.row).altera_valor(True, p.column)

        # Movimento especial Rook
        if self.move_count == 0 and not self.__chess_match.check:
            # Rook pelo lado do rei
            position_tower = Position(self._position.row, self._position.column + 3)
            if self.__test_rook(position_tower):
                p1 = Position(self._position.row, self._position.column + 1)
                p2 = Position(self._position.row, self._position.column + 2)
                if self.board.piece(p1.row, p1.column) == None and self.board.piece(p2.row, p2.column) == None:
                    mat.retorna_elemento(self._position.row).altera_valor(True, self._position.column + 2)

            # Rook pelo lado da rainha
            position_tower = Position(self._position.row, self._position.column - 4)
            if self.__test_rook(position_tower):
                p1 = Position(self._position.row, self._position.column - 1)
                p2 = Position(self._position.row, self._position.column - 2)
                p3 = Position(self._position.row, self._position.column - 3)
                if self.board.piece(p1.row, p1.column) == None and self.board.piece(p2.row, p2.column) == None and self.board.piece(p3.row, p3.column) == None:
                    mat.retorna_elemento(self._position.row).altera_valor(True, self._position.column - 2)

        return mat