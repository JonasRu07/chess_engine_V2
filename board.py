class GameBoard(object):
    """
    A class that simulates a chess board with different additional information
    board:str all fields with every row separated by "/"
    fen:str board representation in official chess notation
    black:bin if a black piece in on the field
    white:bin if a white piece in on the field
    attacked_by_black:bin if a fields is attacked by black
    attacked_by_white:bin if a fields is attacked by white
    fields_with_piece:bi if a piece is on a field
    :arg ref_board:str if a custom board should be used; assumed to be all empty
    :arg ref_fen:str if a custom fen should be used; assumed to ba all empty board
    """
    def __init__(self,
                 ref_board:str = '00000000/00000000/00000000/00000000/00000000/00000000/00000000/00000000',
                 ref_fen:str = '8/8/8/8/8/8/8/8'):
        self.board = ref_board
        self.fen = ref_fen
        self.black = 0b0
        self.white = 0b0
        self.attacked_by_black = 0b0
        self.attacked_by_white = 0b0
        self.fields_with_piece = 0b01

    def update_fields_with_piece(self) -> None:
        """
        updates fields with pieces if there is a piece on it or not
        :return: None
        """
        self.fields_with_piece = 0b0
        for i in range(64):
            self.fields_with_piece = self.fields_with_piece << 1
            if (self.black >> i) % 2 == 1 or (self.white >> i) % 2 == 1:
                self.fields_with_piece += 1