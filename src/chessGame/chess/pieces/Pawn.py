from .. import ChessPiece
from chessGame.boardgame.Position import Position
from estruturasDeDados import ListaDuplamenteEncadeada as Lista
import copy

class Pawn(ChessPiece.ChessPiece):

    def __init__(self, board, color, chess_match):
        super().__init__(board, color)
        self.__chess_match = chess_match
        self.__value = 100
        self.__square_table = [
            [ 0,  0,  0,  0,  0,  0,  0,  0],
            [50, 50, 50, 50, 50, 50, 50, 50],
            [10, 10, 20, 30, 30, 20, 10, 10],
            [ 5,  5, 10, 25, 25, 10,  5,  5],
            [ 0,  0,  0, 20, 20,  0,  0,  0],
            [ 5, -5,-10,  0,  0,-10, -5,  5],
            [ 5, 10, 10,-20,-20, 10, 10,  5],
            [ 0,  0,  0,  0,  0,  0,  0,  0]
        ]

    # Sobrecarga toString
    def __str__(self):
        return 'p' if self.color == 'BLACK' else 'P'

    # Sobrecarga get_evaluation
    def get_evaluation(self, position):
        return self.__square_table[position.row if self.color == 'WHITE' else 7 - position.row][position.column] + self.__value

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = Lista.Lista(8, copy.copy(Lista.Lista(8, False)))

        if self.color == 'WHITE':
            # Movimento para cima (1 casa)
            p = Position(self._position.row - 1, self._position.column)
            if self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento para cima (2 casa)
            p = Position(self._position.row - 2, self._position.column)
            p2 = Position(self._position.row - 1, self._position.column)
            if self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p) and self.board.is_position_exists(p2.row, p2.column) and not self.board.is_there_a_piece(p2) and self.move_count == 0:
                mat.retorna_elemento(p.row).altera_valor(True, p.column)
            
            # Movimento para comer peça adversária (esquerda)
            p = Position(self._position.row - 1, self._position.column - 1)
            if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento para comer peça adversária (direita)
            p = Position(self._position.row - 1, self._position.column + 1)
            if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento especial en passant
            if self._position.row == 3:
                left_pawn = Position(self._position.row, self._position.column - 1)
                if self.board.is_position_exists(left_pawn.row, left_pawn.column) and self._is_there_opponent_piece(left_pawn) and self.board.piece(left_pawn.row, left_pawn.column) == self.__chess_match.en_passant_vulnerable:
                    mat.retorna_elemento(left_pawn.row - 1).altera_valor(True, left_pawn.column)

                right_pawn = Position(self._position.row, self._position.column + 1)
                if self.board.is_position_exists(right_pawn.row, right_pawn.column) and self._is_there_opponent_piece(right_pawn) and self.board.piece(right_pawn.row, right_pawn.column) == self.__chess_match.en_passant_vulnerable:
                    mat.retorna_elemento(right_pawn.row - 1).altera_valor(True, right_pawn.column)

        else:
            # Movimento para cima (1 casa)
            p = Position(self._position.row + 1, self._position.column)
            if self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento para cima (2 casa)
            p = Position(self._position.row + 2, self._position.column)
            p2 = Position(self._position.row + 1, self._position.column)
            if self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p) and self.board.is_position_exists(p2.row, p2.column) and not self.board.is_there_a_piece(p2) and self.move_count == 0:
                mat.retorna_elemento(p.row).altera_valor(True, p.column)
            
            # Movimento para comer peça adversária (esquerda)
            p = Position(self._position.row + 1, self._position.column - 1)
            if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento para comer peça adversária (direita)
            p = Position(self._position.row + 1, self._position.column + 1)
            if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
                mat.retorna_elemento(p.row).altera_valor(True, p.column)

            # Movimento especial en passant
            if self._position.row == 4:
                left_pawn = Position(self._position.row, self._position.column - 1)
                if self.board.is_position_exists(left_pawn.row, left_pawn.column) and self._is_there_opponent_piece(left_pawn) and self.board.piece(left_pawn.row, left_pawn.column) == self.__chess_match.en_passant_vulnerable:
                    mat.retorna_elemento(left_pawn.row + 1).altera_valor(True, left_pawn.column)

                right_pawn = Position(self._position.row, self._position.column + 1)
                if self.board.is_position_exists(right_pawn.row, right_pawn.column) and self._is_there_opponent_piece(right_pawn) and self.board.piece(right_pawn.row, right_pawn.column) == self.__chess_match.en_passant_vulnerable:
                    mat.retorna_elemento(right_pawn.row + 1).altera_valor(True, right_pawn.column)
            
        return mat