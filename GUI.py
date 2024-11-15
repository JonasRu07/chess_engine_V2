import tkinter as tk
import random as rnd

class GUI(object):
    """
    A class for the graphical user interface \n
    window:tk.TK the root window for all further interface parts \n
    images: dict a dictionary that holds all images that are used in the gui \n
    list_of_fields:list[tk.Button] all buttons of the board

    """
    def __init__(self):
        self.controller = None
        self.game_board = None

        self.window = tk.Tk()
        self.window.geometry("1024x1024+-1800+355")
        self.window.title("Chess engine")
        self.images = {
            'pieces' : [
                # https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent  2024|10|18
                tk.PhotoImage(file="./images/black_none_piece.png"),
                tk.PhotoImage(file="./images/black_bishop.png"),
                tk.PhotoImage(file="./images/black_king.png"),
                tk.PhotoImage(file="./images/black_knight.png"),
                tk.PhotoImage(file="./images/black_pawn.png"),
                tk.PhotoImage(file="./images/black_queen.png"),
                tk.PhotoImage(file="./images/black_rook.png"),
                tk.PhotoImage(file='./images/error_piece.png'),
                tk.PhotoImage(file="./images/white_none_piece.png"),
                tk.PhotoImage(file="./images/white_bishop.png"),
                tk.PhotoImage(file="./images/white_king.png"),
                tk.PhotoImage(file="./images/white_knight.png"),
                tk.PhotoImage(file="./images/white_pawn.png"),
                tk.PhotoImage(file="./images/white_queen.png"),
                tk.PhotoImage(file="./images/white_rook.png"),
                tk.PhotoImage(file='./images/error_piece.png')
            ]
        }

        self.list_of_fields = []
        for i in range(64):
            tmp_var = i%8-1 if i//8%2 == 0 else i%8
            color, active_color = ("#FFD39B", "#66CDAA") if tmp_var%2 == 1 else ("#8B5A2B", "#00868B")
            self.list_of_fields.append(
                tk.Button(master=self.window,
                          bg = color,
                          command=lambda idx=i: self.field_click(idx),
                          activebackground= active_color
                          )
                )
            self.list_of_fields[i].place(y=(125*(i//8))+12, x=(125*(i%8))+12, width=125, height=125)

    def field_click(self, index):
        self.list_of_fields[index].config(image=rnd.choice(self.images.get('pieces')))

    def load_board(self):
        """
        loads the board from the reference game_board
        :return: None
        """
        for index_1, line in enumerate(self.game_board.board.split('/')):
            for index_2, piece in enumerate(line):
                if piece != '0':
                    piece_id = self.game_board.dict_piece_id.get(piece)
                    self.list_of_fields[index_1*8 + index_2].config(image=self.images.get('pieces')[piece_id])

    def mainloop(self):
        self.window.mainloop()

    def set_board(self, ref_board):
        self.game_board = ref_board

    def set_controller(self, ref_controller):
        self.controller = ref_controller