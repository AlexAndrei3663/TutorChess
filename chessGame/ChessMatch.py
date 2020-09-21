from ChessException import ChessException
import Board
import ChessPosition
import Rook
import King

# Tabuleiro visível ao jogador
class ChessMatch:

    def __init__(self):
        self.__board = Board.Board(8, 8)
        self.initial_setup()

    # Retorna a matriz com as peças
    def pieces(self):
        mat = []

        for i in range(self.__board.columns):
            row = []
            for j in range(self.__board.columns):
                row.append(self.__board.piece(i, j))
            mat.append(row)
        return mat

    # Setup inicial do tabuleiro
    def initial_setup(self):
        self.__place_new_piece('h', 1, Rook.Rook(self.__board, True))
        self.__place_new_piece('a', 1, Rook.Rook(self.__board, True))
        self.__place_new_piece('f', 3, King.King(self.__board, False))

    # Retorna Matriz de movimentos possíveis
    def possible_move(self, source):
        position = source._to_position()
        self.__validate_source_position(position)
        return self.__board.piece(position.row, position.column).possible_moves()

    # Função para posicionar nova peça ja convertendo char/int pra int/int
    def __place_new_piece(self, column, row, piece):
        self.__board.place_piece(piece, ChessPosition.ChessPosition(column, row)._to_position())

    # Função que retorna a peça capturada pelo movimento
    def perform_chess_move(self, source_position, target_position):
        source = source_position._to_position()
        target = target_position._to_position()
        self.__validate_source_position(source)
        self.__validate_target_position(source, target)
        captured_piece = self.__make_move(source, target)
        return captured_piece

    # Função que valida a entrada (origem da peça)
    def __validate_source_position(self, position):
        if not self.__board.is_there_a_piece(position):
            raise ChessException('Não existe peça na posição de origem escolhida')
        if not self.__board.piece(position.row, position.column).is_there_any_possible_move():
            raise ChessException('Não existem movimentos para a peça escolhida')

    # Função que valida a entrada (localização final da peça)
    def __validate_target_position(self, source, target):
        if not self.__board.piece(source.row, source.column).is_possible_move(target):
            raise ChessException('Posição impossível para a peça escolhida')

    # Função responsável pela movimentação
    def __make_move(self, source, target):
        p = self.__board.remove_piece(source)
        captured_piece = self.__board.remove_piece(target)
        self.__board.place_piece(p, target)
        return captured_piece