from BoardException import *

# Classe de excções que são levantadas pelo usuário (forma de validação)
class ChessException(BoardException):

    def __init__(self, message):
        super().__init__(message)