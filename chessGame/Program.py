from UI import UI
from ChessException import ChessException
import ChessMatch

def main():
    tabuleiro = ChessMatch.ChessMatch()

    while True:
        try:
            UI.print_match(tabuleiro)
            print()
            source = UI.read_chess_position('Source: ')
            mat = tabuleiro.possible_move(source)
            UI.print_board_with_moviments(tabuleiro.pieces(), mat)
            print()
            target = UI.read_chess_position('Target: ')
            captured_piece = tabuleiro.perform_chess_move(source, target)

        except ChessException as e:
            print(e)
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    main()