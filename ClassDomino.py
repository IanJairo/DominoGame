import random

# Classe para representar uma peça de dominó


class DominoPiece:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        self.next = None

# Classe para representar um conjunto de peças de dominó


class DominoSet:
    def __init__(self):
        self.head = None
        self.tail = None

    # Adiciona nova peça ao dominó
    def add_piece(self, value1, value2):
        new_piece = DominoPiece(value1, value2)
        if self.head is None:
            self.head = new_piece
            self.tail = new_piece
        else:
            self.tail.next = new_piece
            self.tail = new_piece

    # Remove uma peça ao dominó
    def remove_piece(self, piece):
        current = self.head
        previous = None
        while current is not None:
            if current == piece:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return
            previous = current
            current = current.next

    # Embaralhar
    def shuffle(self):
        pieces = []
        current = self.head

        while current is not None:
            pieces.append(current)
            current = current.next

        random.shuffle(pieces)
        self.head = pieces[0]
        current = self.head

        for i in range(1, len(pieces)):
            current.next = pieces[i]
            current = current.next

        self.tail = current
        self.tail.next = None

    def __iter__(self):
        current = self.head

        while current is not None:
            yield current
            current = current.next

# Classe para representar um jogador


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = DominoSet()
        self.skipped_turn = False  # Inicialmente, o jogador não pulou o turno

    def draw_piece(self, domino_set):
        if domino_set.head is not None:
            piece = domino_set.head
            self.hand.add_piece(piece.value1, piece.value2)
            domino_set.remove_piece(piece)

    # Verifica se o jogador pode jogar alguma peça
    def can_play_piece(self, board):
        for piece in self.hand:
            if board.can_play_piece(piece):
                return True
        return False

    def play_piece(self, piece, board):
        if piece in self.hand:
            if not board.pieces or board.can_play_piece(piece):
                board.play_piece(piece)
                self.hand.remove_piece(piece)
                return True
        return False

    def skip_turn(self):
        self.skipped_turn = True

    def reset_turn(self):
        self.skipped_turn = False

# Classe para representar o tabuleiro de dominó


class DominoBoard:
    def __init__(self):
        self.pieces = []

    def play_piece(self, piece):
        if not self.pieces:
            self.pieces.append(piece)
        elif piece.value1 == self.pieces[0].value1:
            piece.value1, piece.value2 = piece.value2, piece.value1
            self.pieces.insert(0, piece)
        elif piece.value2 == self.pieces[0].value1:
            self.pieces.insert(0, piece)
        elif piece.value1 == self.pieces[-1].value2:
            self.pieces.append(piece)
        elif piece.value2 == self.pieces[-1].value2:
            piece.value1, piece.value2 = piece.value2, piece.value1
            self.pieces.append(piece)

    def can_play_piece(self, piece):
        return piece.value1 == self.pieces[0].value1 or piece.value2 == self.pieces[0].value1 or \
            piece.value1 == self.pieces[-1].value2 or piece.value2 == self.pieces[-1].value2

    def __str__(self):
        return ', '.join(f'[{piece.value1}:{piece.value2}]' for piece in self.pieces)
