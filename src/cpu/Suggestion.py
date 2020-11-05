from chessGame.chess.ChessPosition import ChessPosition
from estruturasDeDados import ArvoreRedBlack as Arvore
from stockfish import Stockfish
import copy

class Suggestion:
    def __init__(self, chess_match):
        self.__chess_match = chess_match
        self.__moviment_tree = Arvore.RedBlackTree()
        self.__stop_thread = False

    def terminate(self):
        self.__stop_thread = True

    def calculate_suggestions(self):
        print('Sugestões: ')
        for _ in range(5):
            stockfish = Stockfish("./src/cpu/stockfish_20090216_x64", 3)
            new_chess_match = copy.deepcopy(self.__chess_match)
            stockfish.set_fen_position(new_chess_match.get_fen_notation())
            new_chess_match.match_moves.limpa_pilha()
            rounds = 0
            while rounds < 18 and (not new_chess_match.checkmate and not new_chess_match.draw):
                moviment = stockfish.get_best_move()
                captured_piece = new_chess_match.perform_chess_move(
                    ChessPosition(moviment[0], int(moviment[1])), 
                    ChessPosition(moviment[2], int(moviment[3]))
                )
                stockfish.set_fen_position(new_chess_match.get_fen_notation())
                rounds += 1
                
                if self.__stop_thread:
                    break

            # new_chess_match.match_moves.mostrar_tras()
            self.__moviment_tree.add(self.get_eval(stockfish, new_chess_match), new_chess_match.match_moves)
            
        moviments = self.__moviment_tree.max3() if new_chess_match.current_player == 'WHITE' else self.__moviment_tree.min3()
        for best in moviments:
            if best.value == 1000.00 or best.value == -1000.00:
                print('CHECK ->', end=' ')
            else:
                print(f'{best.value} -> ', end = '')
            best.data.mostrar_tras()

    @staticmethod
    def get_eval(stockfish, chess_match) -> float:

        stockfish._put(f"position fen {chess_match.get_fen_notation()}\n eval")
        while True:
            text = stockfish._read_line()
            splitted_text = text.split(" ")
            if splitted_text[0] == "Total":
                if float(splitted_text[-1]) < 0.0:
                    eval = (float(splitted_text[-1]) + float(splitted_text[-2]))
                else:
                    eval = (float(splitted_text[-1]) + float(splitted_text[-3]))
                return float('%.2f'%eval)
            elif splitted_text[0] == "Final":
                if splitted_text[-1] == "check)":
                    if "w" in chess_match.get_fen_notation():
                        return 1000.00
                    else:
                        return -1000.00
                else:
                    NameError('Eval nao encontrado')