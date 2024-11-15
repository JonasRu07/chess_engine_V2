from board import GameBoard
from GUI import GUI
from controller import Controller

board = GameBoard()
controller = Controller()
gui = GUI()

controller.set_board(board)
controller.set_gui(gui)
gui.set_board(board)
gui.set_controller(controller)

controller.start_gui()