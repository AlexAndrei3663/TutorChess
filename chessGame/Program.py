import ChessMatch
import UI

def main():
    tabuleiro = ChessMatch.ChessMatch()
    UI.UI.print_board(tabuleiro.pieces())

if __name__ == "__main__":
    main()