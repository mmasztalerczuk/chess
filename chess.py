import math
 
class Board:
 
    def __init__(self, board):
        self.counter = 1
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
 
        if self.board[a][b] == self.wpawn:                                                                             #pionek
            if (a1 == a + 1 or a1 == 3 and a == 1) and math.fabs(b1 - b) < 2:
                self.attack()
                if a1 == 3 and a == 1:
                    if list(self.board[2][b1])[0] == "W" or list(self.board[2][b1])[0] == "B":
                        print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                        self.test()
                if b1 == b and self.attacked[0] == "B":
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()
                if self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()    
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()                                                                                             #/pionek

        if self.board[a][b] == self.bpawn:                                                                             #pionek
            if (a1 == a - 1 or a1 == 4 and a == 6) and math.fabs(b1 - b) < 2:
                self.attack()
                if a1 == 4 and a == 6:
                    if list(self.board[5][b1])[0] == "W" or list(self.board[5][b1])[0] == "B":
                        print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                        self.test()
                if b1 == b and self.attacked[0] == "W":
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()
                if self.attacked[1] == "0" and math.fabs(b - b1) == 1:
                    print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                    self.test()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()
                
        if self.board[a][b] == self.brook or self.board[a][b] == self.wrook:                                                                              #wieza
            if a == a1:
                c = b
                d = b1
                for x in range (int(math.fabs(b1-b))):
                    while b1>c:
                        c= c+1
                        if list(self.board[a1][c])[0] == "W" or list(self.board[a1][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1:
                        c = c-1
                        if list(self.board[a1][c])[0] == "W" or list(self.board[a1][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            if b == b1:
                c = a
                d = a1
                for x in range (int(math.fabs(a1-a))):
                    while a1>c:
                        c= c+1
                        if list(self.board[c][b1])[0] == "W" or list(self.board[c][b1])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>a1:
                        c = c-1
                        if list(self.board[c][b1])[0] == "W" or list(self.board[c][b1])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()                                                                                             #/wieza
 
        if self.board[a][b] == self.bknight or self.board[a][b] == self.wknight:                                                                            #skoczek
            if (a1 == a + 2 and (b1 == b +1 or b1 == b-1)) or (a1 == a - 2 and (b1 == b +1 or b1 == b-1))\
            or (b1 == b + 2 and (a1 == a +1 or a1 == a-1)) or (b1 == b - 2 and (a1 == a +1 or a1 == a-1)):
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()                                                                                             #/skoczek
 
        if self.board[a][b] == self.bbishop or self.board[a][b] == self.wbishop:                                                                             #goniec
            if a1 - a == b1 - a or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - a))\
            or int(math.fabs(a - a1)) == int(math.fabs(b - b1)):
                c = b
                e = a
                d = b1
                f = a1
                for x in range (int(math.fabs(b1-b))):
                    while b1>c and e>a1:
                        c= c+1
                        e =e-1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while b1>c and a1>e:
                        c = c+1
                        e = e+1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1 and e>a1:
                        c = c-1
                        e = e-1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1 and a1>e:
                        c = c-1
                        e = e+1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            else:
                print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                self.test()                                                                                             #/goniec
 
        if self.board[a][b] == self.bqueen or self.board[a][b] == self.wqueen:                                                                               #dama
            if a == a1:
                c = b
                d = b1
                for x in range (int(math.fabs(b1-b))):
                    while b1>c:
                        c= c+1
                        if list(self.board[a1][c])[0] == "W" or list(self.board[a1][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1:
                        c = c-1
                        if list(self.board[a1][c])[0] == "W" or list(self.board[a1][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            elif b == b1:
                c = a
                d = a1
                for x in range (int(math.fabs(a1-a))):
                    while a1>c:
                        c= c+1
                        if list(self.board[c][b1])[0] == "W" or list(self.board[c][b1])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>a1:
                        c = c-1
                        if list(self.board[c][b1])[0] == "W" or list(self.board[c][b1])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                self.attack()
                self.board[a1][b1] = w
                self.board[a][b] = " 0 "
                self.test()
            elif a1 - a == b1 - a or a - a1 == b - b1 or int(math.fabs(a1 - a)) == int(math.fabs(b1 - a))\
            or int(math.fabs(a - a1)) == int(math.fabs(b - b1)):
                c = b
                e = a
                d = b1
                f = a1
                for x in range (int(math.fabs(b1-b))):
                    while b1>c and e>a1:
                        c= c+1
                        e =e-1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while b1>c and a1>e:
                        c = c+1
                        e = e+1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1 and e>a1:
                        c = c-1
                        e = e-1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
                    while c>b1 and a1>e:
                        c = c-1
                        e = e+1
                        if e == a1 and  c == b1:
                            break
                        if list(self.board[e][c])[0] == "W" or list(self.board[e][c])[0] == "B":
                            print("Niepoprawne dane, wprowadz wspolrzedne jeszcze raz:" + "\n")
                            self.test()
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

    def turns(self):  
        self.attacking = list(self.board[self.a][self.b])
        if self.counter%2 == 0:
            tura = "czarne"
        if self.counter%2 == 1:
            tura = "biale"
        
        if self.win == 0:
            print ("Ruszają się: " + tura)
            if tura == "biale":
                if self.attacking[0] == "W":
                    self.counter +=1
                    print (self.counter, tura)
                else:
                    print ("Powinny sie ruszac biale!!")
                    self.test()
                    
            elif tura == "czarne":
                if self.attacking[0] == "B":
                    self.counter +=1
                    print (self.counter, tura)
                else:
                    print ("Powinny sie ruszac czarne!!")
                    self.test()
            else:
                print ("Zle dane")
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
        self.win = 0
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
        self.turns()
        self.rules()
        test()
 
 
x = Board([])
x.test()
