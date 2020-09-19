from abc import ABC, abstractmethod

# Classe responsável por implementa a classe Peça abstrata
class Piece(ABC):

    def __init__(self, board):
        self.__board = board
        self._position = None

    # Getter do atributo position
    @property
    def board(self):
        return self._position

    # Método abstrato a ser implementado em classes filhas
    @abstractmethod
    def possible_moves(self):
        pass

    #  Retorna True ou False para a posição passada
    def is_possible_move(self, position):
        return self.possible_moves()[position.row][position.column]