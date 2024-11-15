class GameBoard(object):
    """
    A class that simulates a chess board with different additional information
    board:str all fields with every row separated by "/"
    fen:str board representation in official chess notation \n
    black:bin if a black piece in on the field \n
    white:bin if a white piece in on the field \n
    attacked_by_black:bin if a fields is attacked by black \n
    attacked_by_white:bin if a fields is attacked by white \n
    fields_with_piece:bin if a piece is on a field \n
    dict_piece_id:dict dictionary of what piece (fen-notation) has which int value \n
    :arg ref_board:str if a custom board should be used; assumed to be all empty
    :arg ref_fen:str if a custom fen should be used; assumed to ba all empty board
    """
    def __init__(self,
                 ref_board:str = 'rnbqkbnr/pppppppp/00000000/00000000/00000000/00000000/PPPPPPPP/RNBQKBNR',
                 ref_fen:str = '8/8/8/8/8/8/8/8'):

        self.board = ref_board
        self.fen = ref_fen
        self.black = 0b0
        self.white = 0b0
        self.attacked_by_black = 0b0
        self.attacked_by_white = 0b0
        self.fields_with_piece = 0b01
        self.dict_piece_id:dict = {
            'b' : 1,
            'k' : 2,
            'n' : 3,
            'p' : 4,
            'q' : 5,
            'r' : 6,
            'B' : 9,
            'K' : 10,
            'N' : 11,
            'P' : 12,
            'Q' : 13,
            'R' : 14
        }

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
