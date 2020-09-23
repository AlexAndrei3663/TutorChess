import ChessPiece
import Position
import Rook

class King(ChessPiece.ChessPiece):

    def __init__(self, board, color, chess_match):
        super().__init__(board, color)
        self.__chess_match = chess_match

    # Sobrecarga toString
    def __str__(self):
        return 'k' if self.color == 'WHITE' else 'K'

    # Checa se é possível se movimentar
    def __can_move(self, position):
        p = self.board.piece(position.row, position.column)
        return p == None or p.color != self.color

    # Checa se é possível fazer o rook
    def __test_rook(self, position):
        p = self.board.piece(position.row, position.column)
        return p != None and isinstance(p, Rook.Rook) and p.color == self.color and p.move_count == 0

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

        # Movimento especial Rook
        if self.move_count == 0 and not self.__chess_match.check:
            # Rook pelo lado do rei
            position_tower = Position.Position(self._position.row, self._position.column + 3)
            if self.__test_rook(position_tower):
                p1 = Position.Position(self._position.row, self._position.column + 1)
                p2 = Position.Position(self._position.row, self._position.column + 2)
                if self.board.piece(p1.row, p1.column) == None and self.board.piece(p2.row, p2.column) == None:
                    mat[self._position.row][self._position.column + 2] = True

            # Rook pelo lado da rainha
            position_tower = Position.Position(self._position.row, self._position.column - 4)
            if self.__test_rook(position_tower):
                p1 = Position.Position(self._position.row, self._position.column - 1)
                p2 = Position.Position(self._position.row, self._position.column - 2)
                p3 = Position.Position(self._position.row, self._position.column - 3)
                if self.board.piece(p1.row, p1.column) == None and self.board.piece(p2.row, p2.column) == None and self.board.piece(p3.row, p3.column):
                    mat[self._position.row][self._position.column - 2] = True

        return mat