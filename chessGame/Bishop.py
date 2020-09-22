import ChessPiece
import Position

class Bishop(ChessPiece.ChessPiece):

    def __init__(self, board, color):
        super().__init__(board, color)

    # Sobrecarga toString
    def __str__(self):
        return 'b' if self.color == 'WHITE' else 'B'

    # Sobrecarga possible_moves
    def possible_moves(self):
        mat = [[False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8, [False]*8]

        # Movimentos pra cima/direita
        p = Position.Position(self._position.row - 1, self._position.column + 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row - 1, p.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra cima/esquerda
        p = Position.Position(self._position.row - 1, self._position.column - 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row - 1, p.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/direita
        p = Position.Position(self._position.row + 1, self._position.column + 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row + 1, p.column + 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        # Movimentos pra baixo/esquerda
        p = Position.Position(self._position.row + 1, self._position.column - 1)
        while self.board.is_position_exists(p.row, p.column) and not self.board.is_there_a_piece(p):
            mat[p.row][p.column] = True
            p.values(p.row + 1, p.column - 1)
        if self.board.is_position_exists(p.row, p.column) and self._is_there_opponent_piece(p):
            mat[p.row][p.column] = True

        return mat