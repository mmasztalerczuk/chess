from all_figures import *


class Board:
    def __init__(self, board):

        # creating board
        square = " 0 "
        self.board = board
        self.board = [[square for i in range(8)] for j in range(8)]
        self.bpawn = "BP "
        self.brook = "BR "
        self.bknight = "BH "
        self.bbishop = "BB "
        self.bqueen = "BQ "
        self.bking = "BK "
        self.wpawn = "WP "
        self.wrook = "WR "
        self.wknight = "WH "
        self.wbishop = "WB "
        self.wqueen = "WQ "
        self.wking = "WK "

        # setting-up figures
        for i in range(8):
            self.board[1].pop(0)
            self.board[1].append(self.wpawn)
            self.board[6].pop(0)
            self.board[6].append(self.bpawn)

        self.board[0][0] = self.wrook
        self.board[0][1] = self.wknight
        self.board[0][2] = self.wbishop
        self.board[0][3] = self.wqueen
        self.board[0][4] = self.wking
        self.board[0][5] = self.wbishop
        self.board[0][6] = self.wknight
        self.board[0][7] = self.wrook
        self.board[7][0] = self.brook
        self.board[7][1] = self.bknight
        self.board[7][2] = self.bbishop
        self.board[7][4] = self.bqueen
        self.board[7][3] = self.bking
        self.board[7][5] = self.bbishop
        self.board[7][6] = self.bknight
        self.board[7][7] = self.brook

        # pep-8 restrictions
        self.pos_start_a = None
        self.pos_start_b = None
        self.figure = None
        self.attacking = None
        self.attacked = None
        self.pos_end_a = None
        self.pos_end_b = None
        self.check = None
        self.win = 0
        self.tura = None
        self.counter = 1

        # variables to find position of a figure
        self.bking_a = 0
        self.bking_b = 0
        self.wking_a = 0
        self.wking_b = 0
        self.brook_a = 0
        self.brook_b = 0

    # function looping over turns
    def test(self):
        self.win = 0
        # printing board
        for i in self.board:
            print(''.join(i))

        # first input
        cords_start = input("Podaj wspolrzedne poczatkowe:")

        # restarting game
        if cords_start == "restart":
            restart = Board([])
            restart.test()

        # changing input into cords
        cords_start = list(cords_start)
        self.pos_start_a = int(cords_start[0])
        self.pos_start_b = int(cords_start[1])

        # checking if chosen position is a figure
        self.figure = self.board[self.pos_start_a][self.pos_start_b]
        if self.figure == " 0 ":
            print("wybierz pole z figurą!")
            self.test()
        print(self.figure)

        # second input
        cords_end = input("Podaj wspolrzedne docelowe:")

        # restarting game
        if cords_end == "restart":
            restart = Board([])
            restart.test()

        # changing input into cords
        cords_end = list(cords_end)
        self.pos_end_a = int(cords_end[0])
        self.pos_end_b = int(cords_end[1])
        rules(self)

        # repeat
        self.test()

x = Board([])
x.test()
