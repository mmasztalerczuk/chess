import math
<<<<<<< HEAD
 
class Board:
 
    def __init__(self, board):
        square = " 0 "
        self.board = board
        self.board = [[square for j in range(8)] for i in range(8)]
        self.bpawn = "BP "
        self.brook = "BR "
        self.bknight = "BH " 
=======


class Board:
    def __init__(self, board):

        # creating board
        square = " 0 "
        self.board = board
        self.board = [[square for i in range(8)] for j in range(8)]
        self.bpawn = "BP "
        self.brook = "BR "
        self.bknight = "BH "
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
        self.bbishop = "BB "
        self.bqueen = "BQ "
        self.bking = "BK "
        self.wpawn = "WP "
        self.wrook = "WR "
        self.wknight = "WH "
        self.wbishop = "WB "
        self.wqueen = "WQ "
        self.wking = "WK "
<<<<<<< HEAD
=======

        # setting-up figures
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
        for i in range(8):
            self.board[1].pop(0)
            self.board[1].append(self.wpawn)
            self.board[6].pop(0)
            self.board[6].append(self.bpawn)
<<<<<<< HEAD
 
=======

>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
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
<<<<<<< HEAD
 
    def rules(self):
        a = self.a
        b = self.b
        a1 = self.a1
        b1 = self.b1
        w = self.w
 
        if self.board[a][b] == self.wpawn:
            if a1 == a + 1 or a1 == 3 and a == 1:
                self.attack()
                if b1 == b and self.attacked[0] == "W" or b1 == b and self.attacked[0] == "B":
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()           
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()

        if self.board[a][b] == self.bpawn:
            if a1 == a - 1 or a1 == 4 and a == 6:
                self.attack()
                if b1 == b and self.attacked[0] == "W" or b1 == b and self.attacked[0] == "B":
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
                
        if self.board[a][b] == self.brook or self.board[a][b] == self.wrook:
=======

        # pep-8 restrictions
        self.pos_start_a = None
        self.pos_start_b = None
        self.figure = None
        self.attacking = None
        self.attacked = None
        self.pos_end_a = None
        self.pos_end_b = None

    def find(self):
        # finding position of black king
        for self.bking_a, lst in enumerate(self.board):
            for self.bking_b, lst2 in enumerate(lst):
                if lst2 == self.bking:
                    return self.bking_a, self.bking_b

        # finding position of white king
        for self.wking_a, lst in enumerate(self.board):
            for self.wking_b, lst2 in enumerate(lst):
                if lst2 == self.wking:
                    return self.wking_a, self.wking_b

    def rules(self):
        # function with rules for every figure
        """
        a,b - starting positions of figure
        a1,b1 - ending positions of figure
        w - name of selected figure 
        """
        a = self.pos_start_a
        b = self.pos_start_b
        a1 = self.pos_end_a
        b1 = self.pos_end_b
        w = self.figure
        self.find()

        # WHITE PAWN
        if self.board[a][b] == self.wpawn:
            if (a1 == a + 1 or a1 == 3 and a == 1) and math.fabs(b1 - b) < 2:
                self.attack()

                # moving 2 squares from starting position
                if a1 == 3 and a == 1:
                    if list(self.board[2][b1])[0] == "W" or list(self.board[2][b1])[0] == "B":
                        self.error()

                # not "walking" into enemy figures or jumping over them
                if b1 == b and self.attacked[0] == "B" or self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                    self.error()

                # check on black king
                if (self.board[a1 + 1][b1 + 1] or self.board[a1 + 1][b1 - 1]) == self.bking:
                    print("Szach")

                # if all rules are completed - move to destined location
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            # exception handling for other combinations
            else:
                self.error()

                # BLACK PAWN
        if self.board[a][b] == self.bpawn:
            if (a1 == a - 1 or a1 == 4 and a == 6) and math.fabs(b1 - b) < 2:
                self.attack()

                # moving 2 squares from starting position
                if a1 == 4 and a == 6:
                    if list(self.board[5][b1])[0] == "W" or list(self.board[5][b1])[0] == "B":
                        self.error()

                # not "walking" into enemy figures or jumping over them
                if b1 == b and self.attacked[0] == "W" or self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                    self.error()

                # check on white king
                if (self.board[a1 - 1][b1 + 1] or self.board[a1 - 1][b1 - 1]) == self.wking:
                    print("Szach")

                # if all rules are completed - move to destined location
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            # exception handling for other combinations
            else:
                self.error()

        # BLACK AND WHITE ROOK
        if self.board[a][b] == self.brook or self.board[a][b] == self.wrook:

            # moving horizontal
            if a == a1:
                tmp_b = b
                tmp1_a = 0
                tmp1_b = 0

                # preventing from jumping over other figures
                for q in range(int(math.fabs(b1 - b))):
                    while b1 > tmp_b:
                        tmp_b = tmp_b + 1
                        if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                            self.error()
                    while tmp_b > b1:
                        tmp_b = tmp_b - 1
                        if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                            self.error()

                # checking black king
                for l in range(8):
                    if self.board[tmp1_a][b1] == self.bking:
                        print("szach pion - ruch poziomy")
                    tmp1_a = tmp1_a + 1
                    if self.board[a1][tmp1_b] == self.bking:
                        print("szach poziom - ruch poziomy")
                    tmp1_b = tmp1_b + 1

                # if all rules are completed - move to destined location
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
<<<<<<< HEAD
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bknight or self.board[a][b] == self.wknight:                                                                            #skoczek
            if (a1 == a + 2 and b1 == b +1 or b1 == b-1) or (a1 == a - 2 and b1 == b +1 or b1 == b-1)\
            or (b1 == b + 2 and a1 == a +1 or a1 == a-1) or (b1 == b - 2 and a1 == a +1 or a1 == a-1):
=======

            # moving vertical
            if b == b1:
                tmp_a = a
                tmp1_a = 0
                tmp1_b = 0

                # preventing from jumping over other figures
                for v in range(int(math.fabs(a1 - a))):
                    while a1 > tmp_a:
                        tmp_a = tmp_a + 1
                        if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                            self.error()
                    while tmp_a > a1:
                        tmp_a = tmp_a - 1
                        if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                            self.error()

                # checking black king
                for p in range(8):
                    if self.board[tmp1_a][b1] == self.bking:
                        print("szach pion - ruch pionowy")
                    tmp1_a = tmp1_a + 1
                    if self.board[a1][tmp1_b] == self.bking:
                        print("szach poziom - ruch poziomy")
                    tmp1_b = tmp1_b + 1

                # if all rules are completed - move to destined location
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
<<<<<<< HEAD
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bbishop or self.board[a][b] == self.wbishop:                                                                           #goniec
            if a1 - a == b1 - a or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - a))\
            or int(math.fabs(a - a1)) == int(math.fabs(b - b1)):
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bqueen or self.board[a][b] == self.wqueen:                                                                               #dama
            if (a1 - a == b1 - a or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - a))\
            or int(math.fabs(a - a1)) == int(math.fabs(b - b1))) or (a == a1 or b == b1):
=======

            # exception handling for other combinations
            else:
                self.error()

        # BLACK AND WHITE KNIGHT
        if self.board[a][b] == self.bknight or self.board[a][b] == self.wknight:
            if (a1 == a + 2 and (b1 == b + 1 or b1 == b - 1)) or (a1 == a - 2 and (b1 == b + 1 or b1 == b - 1)) \
                    or (b1 == b + 2 and (a1 == a + 1 or a1 == a - 1)) or (b1 == b - 2 and (a1 == a + 1 or a1 == a - 1)):
                self.attack()

                # checking black king
                if self.board[a][b] == self.wknight:
                    try:
                        if (self.board[a1 + 2][b1 + 1] or self.board[a1 + 2][b1 - 1] or self.board[a1 - 2][b1 + 1]
                            or self.board[a1 - 2][b1 - 1] or self.board[a1 + 1][b1 + 2] or self.board[a1 + 1][b1 - 2]
                                or self.board[a1 - 1][b1 + 2] or self.board[a1 - 1][b1 - 2]) == self.bking:
                            print("szach koń - bialy krol")
                    except IndexError:
                        print("szach bialy kon krawedz")

                # checking white king
                if self.board[a][b] == self.bknight:
                    try:
                        if (self.board[a1 + 2][b1 + 1] or self.board[a1 + 2][b1 - 1] or self.board[a1 - 2][b1 + 1]
                            or self.board[a1 - 2][b1 - 1] or self.board[a1 + 1][b1 + 2] or self.board[a1 + 1][b1 - 2]
                                or self.board[a1 - 1][b1 + 2] or self.board[a1 - 1][b1 - 2]) == self.wking:
                            print("szach koń-czarny krol")
                    except IndexError:
                        print("szach czarny kon krawedz")

                # if all rules are completed - move to destined location
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            # exception handling for other combinations
            else:
                self.error()

        # BLACK AND WHITE BISHOP
        if self.board[a][b] == self.bbishop or self.board[a][b] == self.wbishop:
            if a1 - a == b1 - b or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - b)) \
                    or (int(math.fabs(a - a1)) == int(math.fabs(b - b1))):
                self.attack()

                # checking white king
                if self.board[a][b] == self.bbishop:
                    tmp_a = self.wking_a
                    tmp_b = self.wking_b
                    if (tmp_b - b1 == tmp_a - a1 or b1 - tmp_b == a1 - tmp_a) \
                            or (int(math.fabs(tmp_b - b1)) == int(math.fabs(tmp_a - a1))) \
                            or (int(math.fabs(b1 - tmp_b)) == int(math.fabs(a1 - tmp_a))) == self.wking:
                        print("goniec czarny")

                # checking black king
                if self.board[a][b] == self.wbishop:
                    tmp_a = self.bking_a
                    tmp_b = self.bking_b
                    if (tmp_b - b1 == tmp_a - a1) or (b1 - tmp_b == a1 - tmp_a) \
                            or (int(math.fabs(tmp_b - b1)) == int(math.fabs(tmp_a - a1))) \
                            or (int(math.fabs(b1 - tmp_b)) == int(math.fabs(a1 - tmp_a))) == self.bking:
                        print("goniec bialy")

                # if all rules are completed - move to destined location
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            # exception handling for other combinations
            else:
                self.error()

        # BLACK AND WHITE QUEEN
        if self.board[a][b] == self.bqueen or self.board[a][b] == self.wqueen:
            self.find()

            # moving horizontal
            if a == a1:
                tmp_b = b
                tmp1_a = 0
                tmp1_b = 0

                # preventing from jumping over other figures
                for q in range(int(math.fabs(b1 - b))):
                    while b1 > tmp_b:
                        tmp_b = tmp_b + 1
                        if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                            self.error()
                    while tmp_b > b1:
                        tmp_b = tmp_b - 1
                        if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                            self.error()

                # checking black king
                for l in range(8):
                    if self.board[tmp1_a][b1] == self.bking:
                        print("szach pion - ruch poziomy")
                    tmp1_a = tmp1_a + 1
                    if self.board[a1][tmp1_b] == self.bking:
                        print("szach poziom - ruch poziomy")
                    tmp1_b = tmp1_b + 1

                # if all rules are completed - move to destined location
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            if b == b1:
                tmp_a = a
                tmp1_a = 0
                tmp1_b = 0

                # preventing from jumping over other figures
                for v in range(int(math.fabs(a1 - a))):
                    while a1 > tmp_a:
                        tmp_a = tmp_a + 1
                        if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                            self.error()
                    while tmp_a > a1:
                        tmp_a = tmp_a - 1
                        if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                            self.error()

                # checking black king
                for p in range(8):

                    if self.board[tmp1_a][b1] == self.bking:
                        print("szach pion - ruch pionowy")
                        tmp1_a = tmp1_a + 1
                    if self.board[a1][tmp1_b] == self.bking:
                        print("szach poziom - ruch poziomy")
                        tmp1_b = tmp1_b + 1

                # if all rules are completed move to destined location
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
<<<<<<< HEAD
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bking or self.board[a][b] == self.wking:
            if (a1 == a and b1 == b +1) or (a1 == a and b1 == b -1) or (b1 == b and a1 == a -1)\
            or (b1 == b and a1 == a +1) or int(math.fabs(a1 == b1)) == 1:
=======

            # moving diagonal
            if a1 - a == b1 - b or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - b)) \
                    or (int(math.fabs(a - a1)) == int(math.fabs(b - b1))):
                self.attack()

                # checking white king
                if self.board[a][b] == self.bqueen:
                    tmp_a = self.wking_a
                    tmp_b = self.wking_b
                    if (tmp_b - b1 == tmp_a - a1 or b1 - tmp_b == a1 - tmp_a) \
                            or (int(math.fabs(tmp_b - b1)) == int(math.fabs(tmp_a - a1))) \
                            or (int(math.fabs(b1 - tmp_b)) == int(math.fabs(a1 - tmp_a))) == self.wking:
                        print("dama czarna")

                # checking black king
                if self.board[a][b] == self.wqueen:
                    tmp_a = self.bking_a
                    tmp_b = self.bking_b
                    if (tmp_b - b1 == tmp_a - a1) or (b1 - tmp_b == a1 - tmp_a) \
                            or (int(math.fabs(tmp_b - b1)) == int(math.fabs(tmp_a - a1))) \
                            or (int(math.fabs(b1 - tmp_b)) == int(math.fabs(a1 - tmp_a))) == self.bking:
                        print("dama biala")

                # if all rules are completed - move to destined location
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()

            # exception handling for other combinations
            self.error()

        # BLACK AND WHITE KING
        if self.board[a][b] == self.bking or self.board[a][b] == self.wking:
            if (a1 == a and b1 == b + 1) or (a1 == a and b1 == b - 1) or (b1 == b and a1 == a - 1) \
                    or (b1 == b and a1 == a + 1) or int(math.fabs(a1 == b1)) == 1:
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
<<<<<<< HEAD
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
                
    def attack(self):
        a = self.a
        b = self.b
        a1 = self.a1
        b1 = self.b1
        w = self.w
        self.attacking = list(self.board[a][b])
        self.attacked = list(self.board[a1][b1])
        if self.attacking[0] == "W" and self.attacked[0] == "W":
            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
            self.test()
        elif self.attacking[0] == "B" and self.attacked[0] == "B":
            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
            self.test()    

                
    def test(self):
        for i in self.board:
            print(''.join(i))
        x = input("Podaj wspolrzedne:")
        if x == "restart":
            x = Board([])
            x.test()
        x = list(x)
        self.a = int(x[0])
        self.b = int(x[1])
        self.w = self.board[self.a][self.b]
        print(self.w)
        x1 = input("Podaj wspolrzedne222:")
        x1 = list(x1)
        self.a1 = int(x1[0])
        self.b1 = int(x1[1])
        self.rules()
        test()
 
 
x = Board([])
x.test()
=======
                self.error()

    # function checking if destined position isn't already taken by figure of the same color
    def attack(self):
        a = self.pos_start_a
        b = self.pos_start_b
        a1 = self.pos_end_a
        b1 = self.pos_end_b
        self.attacking = list(self.board[a][b])
        self.attacked = list(self.board[a1][b1])
        if self.attacking[0] == self.attacked[0]:
            self.error()

    # function printing error
    def error(self):
        print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
        self.test()

    # function looping over turns
    def test(self):

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
        self.rules()

        # repeat
        self.test()


x = Board([])
x.test()
>>>>>>> b18ec9acf21bdbdeca3db7ed54489be59fc4ac84
