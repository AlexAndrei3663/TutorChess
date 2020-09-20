from UI import UI
from ChessException import ChessException
import ChessMatch

def main():
    tabuleiro = ChessMatch.ChessMatch()

    while True:
        try:
            UI.print_board(tabuleiro.pieces())
            print()
            source = UI.read_chess_position('Source: ')
            print()
            target = UI.read_chess_position('Target: ')

            captured_piece = tabuleiro.perform_chess_move(source, target)
            print(captured_piece)

        except ChessException as e:
            print(e)


if __name__ == "__main__":
    main()