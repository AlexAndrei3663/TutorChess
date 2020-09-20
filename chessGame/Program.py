from UI import *
import ChessMatch

def main():
    tabuleiro = ChessMatch.ChessMatch()

    while True:
        UI.print_board(tabuleiro.pieces())
        print()
        source = UI.read_chess_position('Source: ')
        print()
        target = UI.read_chess_position('Target: ')

        captured_piece = tabuleiro.perform_chess_move(source, target)
        print(captured_piece)

if __name__ == "__main__":
    main()