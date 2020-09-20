from BoardException import BoardException

# Classe responsável por armazenar as peças do tabuleiro e todas as suas funções
class Board:

    def __init__(self, rows, columns):
        if rows < 1 or columns < 1:
            raise BoardException('Error criando Board, é necessário ao menos 1 linha e 1 coluna')
        self.__rows = rows
        self.__columns = columns
        self.__pieces = [[None]*columns, [None]*columns, [None]*columns, [None]*columns, [None]*columns, [None]*columns, [None]*columns, [None]*columns] #*rows #

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
        if not self.__is_position_exists(row, column):
            raise BoardException('Posição inexistente')
        return self.__pieces[row][column]

    # Checa no tabuleiro se a position passada esta entre 0 e 7 (8 posições)
    def __is_position_exists(self, row, column):
        return (row >= 0 and row < self.__rows) and (column >= 0 and column < self.__columns)

    # Checa se na position passada existe uma peça. None = não existe peça
    def is_there_a_piece(self, position):
        if not self.__is_position_exists(position.row, position.column):
            raise BoardException('Posição inexistente')
        return self.piece(position.row, position.column) is not None

    # Adiciona peça ao tabuleiro
    def place_piece(self, piece, position):
        if self.is_there_a_piece(position):
            raise BoardException(f'Ja existe peça na posição {position}')
        self.__pieces[position.row][position.column] = piece
        piece._position = position

    # Remove peça do tabuleiro
    def remove_piece(self, position):
        if not self.__is_position_exists(position.row, position.column):
            raise BoardException('Posição inexistente')
        if self.piece(position.row, position.column) is None:
            return None
        aux = self.piece(position.row, position.column)
        aux._position = None
        self.__pieces[position.row][position.column] = None
        return aux
