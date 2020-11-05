from chessGame.chess import ChessException, ChessMatch
from chessGame.chess.ChessPosition import ChessPosition
from application.UI import UI
from application.gui import GUI
from cpu.Suggestion import Suggestion
from stockfish import Stockfish
import threading

def main():
    gui.draw_board()
    gui.draw_pieces()
    gui.parent.mainloop()
    # cpu_suggestions = Suggestion(tabuleiro)
    # thread = threading.Thread(target = cpu_suggestions.calculate_suggestions)
    # thread.start()
    # cpu_suggestions.terminate()
    # thread.join(0)
    UI.print_match(tabuleiro, stockfish)

if __name__ == "__main__":
    tabuleiro = ChessMatch.ChessMatch()
    stockfish = Stockfish("./src/cpu/stockfish_20090216_x64", 2)
    stockfish.set_skill_level(0)
    gui = GUI(tabuleiro, stockfish)
    main()