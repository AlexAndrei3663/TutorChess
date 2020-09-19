import Board

# Tabuleiro visível ao jogador
class ChessMatch:

    def __init__(self):
        self.__board = Board.Board(8, 8)

    # Retorna a matriz com as peças
    def pieces(self):
        mat = [[None]*self.__board.columns]*self.__board.rows
        
        for i in range(self.__board.columns):
            for j in range(self.__board.columns):
                mat[i][j] = self.__board.piece(i, j)
        
        return mat