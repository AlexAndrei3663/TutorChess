import ChessPiece

class Rook(ChessPiece.ChessPiece):

    def __init__(self, board, color):
        super().__init__(board, color)

    # Sobrecarga toString
    def __str__(self):
        if self.color:
            return 'r'
        return 'R'

    # Sobrecarga possible_moves
    def possible_moves(self):
        # mat = [[None]*self.board.columns]*self.board.rows
        mat = []
        return mat
