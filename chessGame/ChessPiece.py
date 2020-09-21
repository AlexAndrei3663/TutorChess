from abc import ABC, abstractmethod
import Piece

# Classe peça que é visível para o jogador
class ChessPiece(Piece.Piece, ABC):
    
    def __init__(self, board, color):
        super().__init__(board)
        self.__color = color
        self.__move_count = 0

    # Getter do atributor cor
    @property
    def color(self):
        return self.__color

    # Getter do atributo contador de movimentos
    @property
    def move_count(self):
        return self.__move_count

    def _is_there_opponent_piece(self, position):
        p = self.board.piece(position.row, position.column)
        return (p != None) and (p.color != self.__color)

    # Aumenta um no contador
    def increase_move_count(self):
        self.__move_count += 1

    # Diminui um no contador
    def decrease_move_count(self):
        self.__move_count -= 1