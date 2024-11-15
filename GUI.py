import tkinter as tk

class GUI(object):
    def __init__(self):
        self.controller = None
        self.board = None

        self.window = tk.Tk()
        self.window.geometry("1024x1024+-1800+355")
        self.window.title("Chess engine")

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
        pass

    def mainloop(self):
        self.window.mainloop()
