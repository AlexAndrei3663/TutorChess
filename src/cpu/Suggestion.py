from chessGame.chess.ChessPosition import ChessPosition
from estruturasDeDados import ArvoreRedBlack as Arvore
from stockfish import Stockfish
import copy

class Suggestion:
    def __init__(self, chess_match):
        self.__chess_match = chess_match
        self.__moviment_tree = Arvore.RedBlackTree()
        self.calculate_suggestions()

    @property
    def moviment_tree(self):
        return self.__moviment_tree

    def calculate_suggestions(self):
        print('Sugestões: ')
        for _ in range(5):
            stockfish = Stockfish("./src/cpu/stockfish_20090216_x64", 3)
            new_chess_match = copy.deepcopy(self.__chess_match)
            stockfish.set_fen_position(new_chess_match.get_fen_notation())
            rounds = 0
            while rounds < 15 and (not new_chess_match.checkmate and not new_chess_match.draw):
                moviment = stockfish.get_best_move()
                captured_piece = new_chess_match.perform_chess_move(
                    ChessPosition(moviment[0], int(moviment[1])), 
                    ChessPosition(moviment[2], int(moviment[3]))
                )
                stockfish.set_fen_position(new_chess_match.get_fen_notation())
                rounds += 1
            self.__moviment_tree.add(stockfish.get_evaluation(1).get("value"), new_chess_match.match_moves)
        self.__moviment_tree.inOrder()