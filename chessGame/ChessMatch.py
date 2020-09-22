from ChessException import ChessException
import Position
import Board
import ChessPosition
import Rook
import King

# Tabuleiro visível ao jogador
class ChessMatch:

    def __init__(self):
        self.__board = Board.Board(8, 8)
        self.__turn = 1
        self.__current_player = 'WHITE'
        self.__pieces_on_the_board = []
        self.__captured_pieces = []
        self.__check = False
        self.__checkmate = False
        self.initial_setup()

    # Getter do atributo turn
    @property
    def turn(self):
        return self.__turn
    
    # Getter do atributo current player
    @property
    def current_player(self):
        return self.__current_player

    # Getter do atributo check
    @property
    def check(self):
        return self.__check

    # Getter do atributo checkmate
    @property
    def checkmate(self):
        return self.__checkmate

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
        self.__place_new_piece('h', 7, Rook.Rook(self.__board, 'WHITE'))
        self.__place_new_piece('d', 1, Rook.Rook(self.__board, 'WHITE'))
        self.__place_new_piece('e', 1, King.King(self.__board, 'WHITE'))

        self.__place_new_piece('b', 8, Rook.Rook(self.__board, 'BLACK'))
        self.__place_new_piece('a', 8, King.King(self.__board, 'BLACK'))

    # Retorna Matriz de movimentos possíveis
    def possible_move(self, source):
        position = source._to_position()
        self.__validate_source_position(position)
        return self.__board.piece(position.row, position.column).possible_moves()

    # Função para posicionar nova peça ja convertendo char/int pra int/int
    def __place_new_piece(self, column, row, piece):
        self.__board.place_piece(piece, ChessPosition.ChessPosition(column, row)._to_position())
        self.__pieces_on_the_board.append(piece)

    # Função que retorna a peça capturada pelo movimento
    def perform_chess_move(self, source_position, target_position):
        source = source_position._to_position()
        target = target_position._to_position()
        self.__validate_source_position(source)
        self.__validate_target_position(source, target)
        captured_piece = self.__make_move(source, target)

        if self.__test_check(self.__current_player):
            self.__undo_move(source, target, captured_piece)
            raise ChessException('Você não pode se botar em check')

        self.__check = True if self.__test_check(self.__opponent_color(self.__current_player)) else False

        if self.__test_checkmate(self.__opponent_color(self.__current_player)):
            self.__checkmate = True
        else:
            self.__next_turn()

        return captured_piece

    # Função que valida a entrada (origem da peça)
    def __validate_source_position(self, position):
        if not self.__board.is_there_a_piece(position):
            raise ChessException('Não existe peça na posição de origem escolhida')
        if self.__current_player != self.__board.piece(position.row, position.column).color:
            raise ChessException('A peça escolhina não é sua')
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

        if (captured_piece != None):
            self.__pieces_on_the_board.remove(captured_piece)
            self.__captured_pieces.append(captured_piece)

        return captured_piece

    #  Função responsável por retornar o movimento
    def __undo_move(self, source, target, captured_piece):
        p = self.__board.remove_piece(target)
        self.__board.place_piece(p, source)

        if captured_piece != None:
            self.__board.place_piece(captured_piece, target)
            self.__captured_pieces.remove(captured_piece)
            self.__pieces_on_the_board.append(captured_piece)

    # Próximo turno
    def __next_turn(self):
        self.__turn += 1
        self.__current_player = 'BLACK' if self.__current_player == 'WHITE' else 'WHITE'

    # Checa a cor inimiga
    def __opponent_color(self, color):
        return 'BLACK' if color == 'WHITE' else 'WHITE'

    # Acha o Rei da cor passada
    def __king(self, color):
        for p in self.__pieces_on_the_board:
            if p.color == color and isinstance(p, King.King):
                return p

    # Testa pra ver se existe check
    def __test_check(self, color):
        king_position = self.__king(color).chess_position()._to_position()
        for p in self.__pieces_on_the_board:
            if p.color == self.__opponent_color(color):
                mat = p.possible_moves()
                if mat[king_position.row][king_position.column]:
                    return True
        return False

    # Testa pra ver se existe checkmate
    def __test_checkmate(self, color):
        if not self.__test_check(color):
            return False

        for p in self.__pieces_on_the_board:
            if p.color == color:
                mat = p.possible_moves()
                for i in range(len(mat)):
                    for j in range(len(mat)):
                        if mat[i][j]:
                            source = p.chess_position()._to_position()
                            target = Position.Position(i, j)
                            captured_piece = self.__make_move(source, target)
                            test_check = self.__test_check(color)
                            self.__undo_move(source, target, captured_piece)
                            if not test_check:
                                return False
        return True