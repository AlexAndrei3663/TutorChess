import Board
import Position

def main():
    tabuleiro = Board.Board(8, 8)
    print(tabuleiro.is_there_a_piece(Position.Position(0, 0)))

if __name__ == "__main__":
    main()