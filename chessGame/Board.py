# Classe responsável por armazenar as peças do tabuleiro e todas as suas funções
class Board:

    def __init__(self, rows, columns):
        self.__rows = rows
        self.__columns = columns
        self.__pieces = [[None]*columns]*rows

    # Getter do atributo rows
    @property
    def rows(self):
        return self.__rows

    # Getter do atributo columns
    @property
    def columns(self):
        return self.__columns

    # Função que retorna a peça no espaço [row][column]
    def piece(self, row, column):
        return self.__pieces[row][column]

    # Checa no tabuleiro se a position passada esta entre 0 e 7 (8 posições)
    def is_position_exists(self, position):
        return position.row >= 0 and position.row < self.__rows and position.column >= 0 and position.column < self.__columns

    # Checa se na position passada existe uma peça. None = não existe peça
    def is_there_a_piece(self, position):
        return self.piece(position.row, position.column) is not None
