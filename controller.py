class Controller(object):
    def __init__(self):
        self.gui = None
        self.board = None

        self.current_player = 'black'

    def field_clicked(self, index):
        print(index)

    def start_gui(self):
        self.gui.mainloop()

    def set_gui(self, ref_gui):
        self.gui = ref_gui

    def set_board(self, ref_board):
        self.board = ref_board