from chess import ChessException, ChessMatch
from application.UI import UI

def main():
    tabuleiro = ChessMatch.ChessMatch()

    while not tabuleiro.checkmate and not tabuleiro.draw:
        try:
            UI.print_match(tabuleiro)
            print()
            source = UI.read_chess_position('Source: ')
            mat = tabuleiro.possible_move(source)
            UI.print_board_with_moviments(tabuleiro.pieces(), mat)
            print()
            target = UI.read_chess_position('Target: ')
            tabuleiro.perform_chess_move(source, target)

            if tabuleiro.promoted != None:
                type = str(input('Digite a peça para promoção (B/N/R/Q): ')).upper()
                while type != 'B' and type != 'N' and type != 'R' and type != 'Q':
                    type = str(input('Digite a peça para promoção (B/N/R/Q): ')).upper()
                tabuleiro.replace_promoted_piece(type)
        except ChessException.ChessException as e:
            print(e)
        except ValueError as e:
            print(e)
    UI.print_match(tabuleiro)

if __name__ == "__main__":
    main()