from chessGame.chess.ChessPosition import ChessPosition
from estruturasDeDados import ArvoreRedBlack as Arvore
from stockfish import Stockfish
import copy

class Suggestion:
    def __init__(self, chess_match):
        self.__chess_match = chess_match
        self.__moviment_tree = Arvore.RedBlackTree()
        # self.stop_thread = False
        self.calculate_suggestions()

    def calculate_suggestions(self):
        print('Sugestões: ')
        for _ in range(5):
            stockfish = Stockfish("./src/cpu/stockfish_20090216_x64", 3)
            new_chess_match = copy.deepcopy(self.__chess_match)
            stockfish.set_fen_position(new_chess_match.get_fen_notation())
            rounds = 0
            while rounds < 18 and (not new_chess_match.checkmate and not new_chess_match.draw):
                moviment = stockfish.get_best_move()
                captured_piece = new_chess_match.perform_chess_move(
                    ChessPosition(moviment[0], int(moviment[1])), 
                    ChessPosition(moviment[2], int(moviment[3]))
                )
                stockfish.set_fen_position(new_chess_match.get_fen_notation())
                rounds += 1

                # if self.stop_thread:
                #     break
            new_chess_match.match_moves.mostrar_tras()
            self.__moviment_tree.add(self.get_eval(stockfish, new_chess_match.get_fen_notation()), new_chess_match.match_moves)
            
        moviments = self.__moviment_tree.max3() if new_chess_match.current_player == 'WHITE' else self.__moviment_tree.min3()
        for best in moviments:
            print(f'{best.value} -> ', end = '')
            best.data.mostrar_tras()

    @staticmethod
    def get_eval(stockfish, fen) -> float:
        if fen is None:
            raise NameError('Notacao fen nao especificada')

        stockfish._put(f"position fen {fen}\n eval")
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
                NameError('Eval nao encontrado')