import ChessPiece
import Position

class King(ChessPiece.ChessPiece):

    def __init__(self, board, color):
        super().__init__(board, color)

    # Sobrecarga toString
    def __str__(self):
        if self.color == 'WHITE':
            return 'k'
        return 'K'

    # Checa se é possível se movimentar
    def __can_move(self, position):
        p = self.board.piece(position.row, position.column)
        return p == None or p.color != self.color

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = [[False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8]

        # Movimentos pra cima
        p = Position.Position(self._position.row - 1, self._position.column)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo
        p = Position.Position(self._position.row + 1, self._position.column)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra direita
        p = Position.Position(self._position.row, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra esquerda
        p = Position.Position(self._position.row, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra cima/direita
        p = Position.Position(self._position.row - 1, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra cima/esquerda
        p = Position.Position(self._position.row - 1, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/direita
        p = Position.Position(self._position.row + 1, self._position.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/esquerda
        p = Position.Position(self._position.row + 1, self._position.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self.__can_move(p):
            mat[p.row][p.column] = True

        return mat