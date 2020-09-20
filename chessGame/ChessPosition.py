import Position

class ChessPosition:

    def __init__(self, column, row):
        if (row < 1 or row > 8) and (column < 'a' or column > 'h'):
            print('Posição invalida, apenas a1 até h8')
            return
        self.__row = row
        self.__column = column

    # Getter do atributo row(int)
    @property
    def row(self):
        return self.__row

    # Getter do atributo column(char)
    @property
    def column(self):
        return self.__column

    # Conversão do formato char/int para int/int(matriz)
    def _to_position(self):
        return Position.Position(8 - self.__row, ord(self.__column) - ord('a'))
    
    def __str__(self):
        return f'{self.__column}{self.__row}'

# 	protected static ChessPosition fromPosition(Position position) {
# 		return new ChessPosition((char)('a' - position.getColumn()), 8 - position.getRow());
# 	}