from .ChessException import ChessException
from .pieces import Bishop, King, Knight, Pawn, Queen, Rook
from boardgame.Position import Position
from boardgame.Board import Board
from .ChessPosition import ChessPosition

# Tabuleiro visível ao jogador
class ChessMatch:

    def __init__(self):
        self.__board = Board(8, 8)
        self.__turn = 1
        self.__current_player = 'WHITE'
        self.__pieces_on_the_board = []
        self.__captured_pieces = []
        self.__turn_move = []
        self.__match_moves = []
        self.__check = False
        self.__checkmate = False
        self.__draw = False
        self.__en_passant_vulnerable = None
        self.__promoted = None
        self.initial_setup()

    # Getter do atributo turn
    @property
    def turn(self):
        return self.__turn
    
    # Getter do atributo current player
    @property
    def current_player(self):
        return self.__current_player

    @property
    def match_moves(self):
        return self.__match_moves

    # Getter do atributo check
    @property
    def check(self):
        return self.__check

    # Getter do atributo checkmate
    @property
    def checkmate(self):
        return self.__checkmate

    @property
    def draw(self):
        return self.__draw

    # Getter do atributo en passant vulnerable
    @property
    def en_passant_vulnerable(self):
        return self.__en_passant_vulnerable

    # 
    @property
    def promoted(self):
        return self.__promoted

    # Retorna a matriz com as peças
    def pieces(self):
        mat = []

        for i in range(self.__board.columns):
            row = []
            for j in range(self.__board.columns):
                row.append(self.__board.piece(i, j))
            mat.append(row)
        return mat

    # Retorna Matriz de movimentos possíveis
    def possible_move(self, source):
        position = source._to_position()
        self.__validate_source_position(position)
        return self.__board.piece(position.row, position.column).possible_moves()

    # Função para posicionar nova peça ja convertendo char/int pra int/int
    def __place_new_piece(self, column, row, piece):
        self.__board.place_piece(piece, ChessPosition(column, row)._to_position())
        self.__pieces_on_the_board.append(piece)

    # Função que retorna a peça capturada pelo movimento
    def perform_chess_move(self, source_position, target_position):
        if self.__current_player == 'WHITE':
            self.__turn_move = []

        source = source_position._to_position()
        target = target_position._to_position()
        self.__validate_source_position(source)
        self.__validate_target_position(source, target)
        captured_piece = self.__make_move(source, target)
        moved_piece = self.__board.piece(target.row, target.column)

         # Movimento especial promoção
        self.__promoted = None
        if isinstance(moved_piece, Pawn.Pawn):
            if (moved_piece.color == 'WHITE' and target.row == 0) or (moved_piece.color == 'BLACK' and target.row == 7):
                self.__promoted = self.__board.piece(target.row, target.column)
                self.__promoted = self.replace_promoted_piece('Q')

        if self.__test_check(self.__current_player):
            self.__undo_move(source, target, captured_piece)
            raise ChessException('O seu rei está em check')

        self.__check = True if self.__test_check(self.__opponent_color(self.__current_player)) else False

        # Cria a lista de movimentos da partida
        # Apenas movimentação
        if captured_piece == None:
            if self.__promoted != None:
                self.__turn_move.append(str(target_position) + str(self.__promoted).upper())
            elif isinstance(moved_piece, Pawn.Pawn):
                self.__turn_move.append(str(source_position))
            # Rook pelo lado do rei
            elif isinstance(moved_piece, King.King) and target.column - source.column == 2:
                self.__turn_move.append('O-O')
            # Rook pelo lado da rainha
            elif isinstance(moved_piece, King.King) and target.column - source.column == -2:
                self.__turn_move.append('O-O-O')
            else:
                self.__turn_move.append(str(moved_piece).upper() + str(source_position))

            # Se estiver em check, o movimento que ocasionou deve ser adicionado um + no final
            if self.__check:
                self.__turn_move[len(self.__turn_move) - 1] += '+'
        # Capturas
        elif captured_piece != None:
            if isinstance(moved_piece, Pawn.Pawn):
                self.__turn_move.append(str(source_position.column) + 'x' + str(target_position))
            else:
                self.__turn_move.append(str(moved_piece) + 'x' + str(target_position))

        if self.__current_player == 'BLACK':
            self.__match_moves.append(self.__turn_move)

        # Testa check e checkmate
        if self.__test_checkmate(self.__opponent_color(self.__current_player)):
            self.__checkmate = True
            self.__turn_move[len(self.__turn_move) - 1] += '+'

            if len(self.__turn_move) == 1:
                self.__match_moves.append(self.__turn_move)
        elif self.__test_draw():
            self.__draw = True
        else:
            self.__next_turn()

        # Movimento especial en passant
        if isinstance(moved_piece, Pawn.Pawn) and (target.row == source.row - 2 or target.row == source.row + 2):
            self.__en_passant_vulnerable = moved_piece
        else:
            self.__en_passant_vulnerable = None

        return captured_piece

    # Troca o peão promovido para a peça escolhida
    def replace_promoted_piece(self, type):
        if type != 'B' and type != 'N' and type != 'R' and type != 'Q':
            return self.__promoted

        promoted_position = self.__promoted.chess_position()._to_position()
        p = self.__board.remove_piece(promoted_position)
        self.__pieces_on_the_board.remove(p)

        new_piece = self.__new_piece(type, self.__promoted.color)
        self.__board.place_piece(new_piece, promoted_position)
        self.__pieces_on_the_board.append(new_piece)

        return new_piece

    # Função que cria nova peça depois que o jogo ja começou
    def __new_piece(self, type, color):
        if type == 'B':
            return Bishop.Bishop(self.__board, color)
        if type == 'N':
            return Knight.Knight(self.__board, color)
        if type == 'Q':
            return Queen.Queen(self.__board, color)
        return Rook.Rook(self.__board, color)

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
        p.increase_move_count()
        captured_piece = self.__board.remove_piece(target)
        self.__board.place_piece(p, target)

        if captured_piece != None:
            self.__pieces_on_the_board.remove(captured_piece)
            self.__captured_pieces.append(captured_piece)

        # Movimento especial rook pelo lado do rei
        if isinstance(p, King.King) and target.column == source.column + 2:
            source_tower = Position(source.row, source.column + 3)
            target_tower = Position(source.row, source.column + 1)
            rook = self.__board.remove_piece(source_tower)
            self.__board.place_piece(rook, target_tower)
            rook.increase_move_count()

        # Movimento especial rook pelo lado da rainha
        if isinstance(p, King.King) and target.column == source.column - 2:
            source_tower = Position(source.row, source.column - 4)
            target_tower = Position(source.row, source.column - 1)
            rook = self.__board.remove_piece(source_tower)
            self.__board.place_piece(rook, target_tower)
            rook.increase_move_count()

        # Movimento especial en passant
        if isinstance(p, Pawn.Pawn):
            if source.column != target.column and captured_piece == None:
                if p.color == 'WHITE':
                    pawn_positon = Position(target.row + 1, target.column)
                else:
                    pawn_positon = Position(target.row - 1, target.column)
                captured_piece = self.__board.remove_piece(pawn_positon)
                self.__captured_pieces.append(captured_piece)
                self.__pieces_on_the_board.remove(captured_piece)

        return captured_piece

    #  Função responsável por retornar o movimento
    def __undo_move(self, source, target, captured_piece):
        p = self.__board.remove_piece(target)
        p.increase_move_count()
        self.__board.place_piece(p, source)

        if captured_piece != None:
            self.__board.place_piece(captured_piece, target)
            self.__captured_pieces.remove(captured_piece)
            self.__pieces_on_the_board.append(captured_piece)

        # Movimento especial rook pelo lado do rei
        if isinstance(p, King.King) and target.column == source.column + 2:
            source_tower = Position(source.row, source.column + 3)
            target_tower = Position(source.row, source.column + 1)
            rook = self.__board.remove_piece(target_tower)
            self.__board.place_piece(rook, source_tower)
            rook.decrease_move_count()

        # Movimento especial rook pelo lado da rainha
        if isinstance(p, King.King) and target.column == source.column - 2:
            source_tower = Position(source.row, source.column - 4)
            target_tower = Position(source.row, source.column - 1)
            rook = self.__board.remove_piece(target_tower)
            self.__board.place_piece(rook, source_tower)
            rook.decrease_move_count()

        # Movimento especial en passant
        if isinstance(p, Pawn.Pawn):
            if source.column != target.column and captured_piece == self.__en_passant_vulnerable:
                pawn = self.__board.remove_piece(target)
                if p.color == 'WHITE':
                    pawn_positon = Position(3, target.column)
                else:
                    pawn_positon = Position(4, target.column)
                self.__board.place_piece(pawn, pawn_positon)

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
                            target = Position(i, j)
                            captured_piece = self.__make_move(source, target)
                            test_check = self.__test_check(color)
                            self.__undo_move(source, target, captured_piece)
                            if not test_check:
                                return False
        return True

    # Testa pra ver se existe empate
    def __test_draw(self):
        # Falta de material (B e K vs K, N e K vs K, K vs K)
        if len(self.__pieces_on_the_board) == 3:
            for p in self.__pieces_on_the_board:
                if isinstance(p, Knight.Knight) or isinstance(p, Bishop.Bishop):
                    return True
        elif len(self.__pieces_on_the_board) == 2:
            print('teste')
            return True
        else:
            # Afogamento
            for p in self.__pieces_on_the_board:
                if p.color == self.__opponent_color(self.__current_player):
                    if p.is_there_any_possible_move() and not isinstance(p, King.King):
                        return False
                    elif isinstance(p, King.King):
                        mat = p.possible_moves()
                        for i in range(len(mat)):
                            for j in range(len(mat)):
                                if mat[i][j]:
                                    source = p.chess_position()._to_position()
                                    target = Position(i, j)
                                    captured_piece = self.__make_move(source, target)
                                    test_check = self.__test_check(self.__opponent_color(self.__current_player))
                                    self.__undo_move(source, target, captured_piece)
                                    if not test_check:
                                        return False
            return True
        return False

    # Setup inicial do tabuleiro
    def initial_setup(self):
        self.__place_new_piece('a', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('b', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('c', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('d', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('e', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('f', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('g', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('h', 2, Pawn.Pawn(self.__board, 'WHITE', self))
        self.__place_new_piece('a', 1, Rook.Rook(self.__board, 'WHITE'))
        self.__place_new_piece('h', 1, Rook.Rook(self.__board, 'WHITE'))
        self.__place_new_piece('c', 1, Bishop.Bishop(self.__board, 'WHITE'))
        self.__place_new_piece('f', 1, Bishop.Bishop(self.__board, 'WHITE'))
        self.__place_new_piece('b', 1, Knight.Knight(self.__board, 'WHITE'))
        self.__place_new_piece('g', 1, Knight.Knight(self.__board, 'WHITE'))
        self.__place_new_piece('d', 1, Queen.Queen(self.__board, 'WHITE'))
        self.__place_new_piece('e', 1, King.King(self.__board, 'WHITE', self))

        self.__place_new_piece('a', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('b', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('c', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('d', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('e', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('f', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('g', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('h', 7, Pawn.Pawn(self.__board, 'BLACK', self))
        self.__place_new_piece('a', 8, Rook.Rook(self.__board, 'BLACK'))
        self.__place_new_piece('h', 8, Rook.Rook(self.__board, 'BLACK'))
        self.__place_new_piece('c', 8, Bishop.Bishop(self.__board, 'BLACK'))
        self.__place_new_piece('f', 8, Bishop.Bishop(self.__board, 'BLACK'))
        self.__place_new_piece('b', 8, Knight.Knight(self.__board, 'BLACK'))
        self.__place_new_piece('g', 8, Knight.Knight(self.__board, 'BLACK'))
        self.__place_new_piece('d', 8, Queen.Queen(self.__board, 'BLACK'))
        self.__place_new_piece('e', 8, King.King(self.__board, 'BLACK', self))