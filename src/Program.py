from chessGame.chess import ChessException, ChessMatch
from chessGame.chess.ChessPosition import ChessPosition
from chessGame.application.UI import UI
from stockfish import Stockfish

def main():
    tabuleiro = ChessMatch.ChessMatch()
    teste = []

    while not tabuleiro.checkmate and not tabuleiro.draw:
        try:
            if tabuleiro.current_player == 'WHITE':
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

                teste.append(source.column + str(source.row) + target.column + str(target.row))
            else:
                moviment = stockfish.get_best_move()
                teste.append(moviment)
                print(f'Movimento: {ChessPosition(moviment[0], int(moviment[1]))} para {ChessPosition(moviment[2], int(moviment[3]))}')
                tabuleiro.perform_chess_move(
                    ChessPosition(moviment[0], int(moviment[1])), 
                    ChessPosition(moviment[2], int(moviment[3]))
                )
            
            stockfish.set_position(teste)
        except ChessException.ChessException as e:
            print(e)
        except ValueError as e:
            print(e)
    UI.print_match(tabuleiro)

if __name__ == "__main__":
    stockfish = Stockfish("./src/cpu/stockfish_20090216_x64")
    stockfish.set_skill_level(3)
    main()