import tkinter as tk
import random as rnd

#TODO change images Pieces in list, so that tey can be accessed by just their id;

class GUI(object):
    def __init__(self):
        self.controller = None
        self.board = None

        self.window = tk.Tk()
        self.window.geometry("1024x1024+-1800+355")
        self.window.title("Chess engine")
        self.images = {
            # https://commons.wikimedia.org/wiki/Category:PNG_chess_pieces/Standard_transparent  2024|10|18
            'b' : tk.PhotoImage(file="./images/black_bishop.png"),
            'k' : tk.PhotoImage(file="./images/black_king.png"),
            'n' : tk.PhotoImage(file="./images/black_knight.png"),
            'p' : tk.PhotoImage(file="./images/black_pawn.png"),
            'q' : tk.PhotoImage(file="./images/black_queen.png"),
            'r' : tk.PhotoImage(file="./images/black_rook.png"),
            'B' : tk.PhotoImage(file="./images/white_bishop.png"),
            'K' : tk.PhotoImage(file="./images/white_king.png"),
            'N' : tk.PhotoImage(file="./images/white_knight.png"),
            'P' : tk.PhotoImage(file="./images/white_pawn.png"),
            'Q' : tk.PhotoImage(file="./images/white_queen.png"),
            'R' : tk.PhotoImage(file="./images/white_rook.png")
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
        self.list_of_fields[index].config(image=rnd.choice(list(self.images.values())))

    def mainloop(self):
        self.window.mainloop()

    def set_board(self, ref_board):
        self.board = ref_board

    def set_controller(self, ref_controller):
        self.controller = ref_controller