import math
from king_checking import find
from errors import *


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
    find(self)
    self.check = 1

    # WHITE PAWN
    if self.board[a][b] == self.wpawn:
        if (a1 == a + 1 or a1 == 3 and a == 1) and math.fabs(b1 - b) < 2:
            self.attack()

            # moving 2 squares from starting position
            if a1 == 3 and a == 1:
                if list(self.board[2][b1])[0] == "W" or list(self.board[2][b1])[0] == "B":
                    error_wrong_square(self)

            # not "walking" into enemy figures or jumping over them
            if b1 == b and self.attacked[0] == "B" or self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                error_wrong_square(self)

            # check on black king
            if (self.board[a1 + 1][b1 + 1] or self.board[a1 + 1][b1 - 1]) == self.bking:
                print("Szach")

            # if all rules are completed - move to destined location
            self.turns()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

        # exception handling for other combinations
        else:
            error_wrong_square(self)

            # BLACK PAWN
    if self.board[a][b] == self.bpawn:
        if (a1 == a - 1 or a1 == 4 and a == 6) and math.fabs(b1 - b) < 2:
            self.attack()

            # moving 2 squares from starting position
            if a1 == 4 and a == 6:
                if list(self.board[5][b1])[0] == "W" or list(self.board[5][b1])[0] == "B":
                    error_wrong_square(self)

            # not "walking" into enemy figures or jumping over them
            if b1 == b and self.attacked[0] == "W" or self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                error_wrong_square(self)

            # check on white king
            if (self.board[a1 - 1][b1 + 1] or self.board[a1 - 1][b1 - 1]) == self.wking:
                print("Szach czarny pionek na bialego krola!")

            # if all rules are completed - move to destined location
            self.turns()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

        # exception handling for other combinations
        else:
            error_wrong_square(self)

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
                    tmp_b += 1
                    if list(self.board[a1][tmp_b])[0] == ("W" or "B"):
                        error_wrong_square(self)
                while tmp_b > b1:
                    tmp_b -= 1
                    if list(self.board[a1][tmp_b])[0] == ("W" or "B"):
                        error_wrong_square(self)

            # checking king
            for l in range(8):
                if self.board[tmp1_a][b1] == (self.bking or self.wking):
                    while tmp1_a - 1 > a1:
                        tmp1_a -= 1
                        if list(self.board[tmp1_a][b1])[0] == ("W" or "B"):
                            self.check = 0

                    while a1 > tmp1_a + 1:
                        tmp1_a += 1
                        if list(self.board[tmp1_a][b1])[0] == ("W" or "B"):
                            self.check = 0
                tmp1_a += 1

                if self.board[a1][tmp1_b] == self.bking:
                    while tmp1_b - 1 > b1:
                        tmp1_b -= 1
                        if list(self.board[a1][tmp1_b])[0] == ("W" or "B"):
                            self.check = 0
                    while b1 > tmp1_b + 1:
                        tmp1_a += 1
                        if list(self.board[a1][tmp1_b])[0] == ("W" or "B"):
                            self.check = 0
                tmp1_b += 1

            # if all rules are completed - move to destined location
            if self.tura == "czarne":
                if list(self.wking)[0] == list(self.board[a][b])[0]:
                    self.check = 0
            if self.tura == "biale":
                if list(self.bking)[0] == list(self.board[a][b])[0]:
                    self.check = 0
            self.turns()
            self.attack()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            if self.check == 1:
                print("SZACH!")
            self.test()

        # moving vertical
        if b == b1:
            tmp_a = a
            tmp1_a = 0
            tmp1_b = 0

            # preventing from jumping over other figures
            for v in range(int(math.fabs(a1 - a))):
                while a1 > tmp_a:
                    tmp_a += 1
                    if list(self.board[tmp_a][b1])[0] == ("W" or "B"):
                        error_wrong_square(self)
                while tmp_a > a1:
                    tmp_a -= 1
                    if list(self.board[tmp_a][b1])[0] == ("W" or "B"):
                        error_wrong_square(self)

            # checking kings
            for l in range(8):
                if self.board[tmp1_a][b1] == (self.bking or self.wking):
                    while tmp1_a - 1 > a1:
                        tmp1_a -= 1
                        if list(self.board[tmp1_a][b1])[0] == ("W" or "B"):
                            self.check = 0

                    while a1 > tmp1_a + 1:
                        tmp1_a += 1
                        if list(self.board[tmp1_a][b1])[0] == ("W" or "B"):
                            self.check = 0
                tmp1_a += 1

                if self.board[a1][tmp1_b] == self.bking:
                    while tmp1_b - 1 > b1:
                        tmp1_b -= 1
                        if list(self.board[a1][tmp1_b])[0] == ("W" or "B"):
                            self.check = 0
                    while b1 > tmp1_b + 1:
                        tmp1_a += 1
                        if list(self.board[a1][tmp1_b])[0] == ("W" or "B"):
                            self.check = 0
                tmp1_b += 1

            # if all rules are completed - move to destined location
            if self.tura == "czarne":
                if list(self.wking)[0] == list(self.board[a][b])[0]:
                    self.check = 0
            if self.tura == "biale":
                if list(self.bking)[0] == list(self.board[a][b])[0]:
                    self.check = 0
            self.turns()
            self.attack()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            if self.check == 1:
                print("SZACH!")
            self.test()

        # exception handling for other combinations
        else:
            error_wrong_square(self)

    # BLACK AND WHITE KNIGHT
    if self.board[a][b] == self.bknight or self.board[a][b] == self.wknight:
        if (a1 == a + 2 and (b1 == b + 1 or b1 == b - 1)) or (a1 == a - 2 and (b1 == b + 1 or b1 == b - 1)) \
                or (b1 == b + 2 and (a1 == a + 1 or a1 == a - 1)) or (b1 == b - 2 and (a1 == a + 1 or a1 == a - 1)):
            self.attack()

            # checking black king
            if self.board[a][b] == self.wknight:
                try:
                    if (self.board[a1 + 2][b1 + 1] or self.board[a1 + 2][b1 - 1] or
                            self.board[a1 - 2][b1 + 1] or self.board[a1 - 2][b1 - 1] or
                            self.board[a1 + 1][b1 + 2] or self.board[a1 + 1][b1 - 2] or
                            self.board[a1 - 1][b1 + 2] or self.board[a1 - 1][b1 - 2]) == self.bking:
                        print("szach koń - bialy krol")
                except IndexError:
                    print("szach bialy kon krawedz")

            # checking white king
            if self.board[a][b] == self.bknight:
                try:
                    if (self.board[a1 + 2][b1 + 1] or self.board[a1 + 2][b1 - 1] or
                            self.board[a1 - 2][b1 + 1] or self.board[a1 - 2][b1 - 1] or
                            self.board[a1 + 1][b1 + 2] or self.board[a1 + 1][b1 - 2] or
                            self.board[a1 - 1][b1 + 2] or self.board[a1 - 1][b1 - 2]) == self.wking:
                        print("szach koń-czarny krol")
                except IndexError:
                    print("szach czarny kon krawedz")

            # if all rules are completed - move to destined location
            self.turns()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

        # exception handling for other combinations
        else:
            error_wrong_square(self)

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
            self.turns()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

        # exception handling for other combinations
        else:
            error_wrong_square(self)

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
                    tmp_b += 1
                    if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                        error_wrong_square(self)
                while tmp_b > b1:
                    tmp_b -= 1
                    if list(self.board[a1][tmp_b])[0] == "W" or list(self.board[a1][tmp_b])[0] == "B":
                        error_wrong_square(self)

            # checking black king
            for l in range(8):
                if self.board[tmp1_a][b1] == self.bking:
                    print("szach pion - ruch poziomy")
                tmp1_a += 1
                if self.board[a1][tmp1_b] == self.bking:
                    print("szach poziom - ruch poziomy")
                tmp1_b += 1

            # if all rules are completed - move to destined location
            self.turns()
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
                    tmp_a += 1
                    if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                        error_wrong_square(self)
                while tmp_a > a1:
                    tmp_a -= 1
                    if list(self.board[tmp_a][b1])[0] == "W" or list(self.board[tmp_a][b1])[0] == "B":
                        error_wrong_square(self)

            # checking black king
            for p in range(8):

                if self.board[tmp1_a][b1] == self.bking:
                    print("szach pion - ruch pionowy")
                    tmp1_a += 1
                if self.board[a1][tmp1_b] == self.bking:
                    print("szach poziom - ruch poziomy")
                    tmp1_b += 1

            # if all rules are completed move to destined location
            self.turns()
            self.attack()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

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
            self.turns()
            self.attack()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()

        # exception handling for other combinations
        error_wrong_square(self)

    # BLACK AND WHITE KING
    if self.board[a][b] == self.bking or self.board[a][b] == self.wking:
        if (a1 == a and b1 == b + 1) or (a1 == a and b1 == b - 1) or (b1 == b and a1 == a - 1) \
                or (b1 == b and a1 == a + 1) or int(math.fabs(a1 == b1)) == 1:
            self.turns()
            self.attack()
            self.board[a1][b1] = w
            self.board[a][b] = " 0 "
            self.test()
        else:
            self.error()
