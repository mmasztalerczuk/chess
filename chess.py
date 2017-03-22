import math
 
class Board:
 
    def __init__(self, board):
        square = " 0 "
        self.board = board
        self.board = [[square for j in range(8)] for i in range(8)]
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
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bknight or self.board[a][b] == self.wknight:                                                                            #skoczek
            if (a1 == a + 2 and b1 == b +1 or b1 == b-1) or (a1 == a - 2 and b1 == b +1 or b1 == b-1)\
            or (b1 == b + 2 and a1 == a +1 or a1 == a-1) or (b1 == b - 2 and a1 == a +1 or a1 == a-1):
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
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
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
 
        if self.board[a][b] == self.bking or self.board[a][b] == self.wking:
            if (a1 == a and b1 == b +1) or (a1 == a and b1 == b -1) or (b1 == b and a1 == a -1)\
            or (b1 == b and a1 == a +1) or int(math.fabs(a1 == b1)) == 1:
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
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