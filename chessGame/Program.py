from UI import *
import ChessMatch

def main():
    tabuleiro = ChessMatch.ChessMatch()
    UI.print_board(tabuleiro.pieces())

if __name__ == "__main__":
    main()