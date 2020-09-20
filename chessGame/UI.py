import ChessPosition

class UI:

    # Printa o Tabuleiro
    @staticmethod
    def print_board(pieces):
        for i in range(len(pieces)):
            print(f'{(8 - i)} ', end='')
            for j in range(len(pieces)):
                UI.print_piece(pieces[i][j])
            print()
        print('  a b c d e f g h')

    # Printa a peça
    @staticmethod
    def print_piece(piece):
        if piece is None:
            print('-', end='')
        else:
            print(piece, end='')
        print(' ', end='')

    @staticmethod
    def read_chess_position(message):
        position = str(input(message))
        return ChessPosition.ChessPosition(position[0], int(position[1:]))