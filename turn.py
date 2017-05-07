def turns(self):
    self.attacking = list(self.board[self.pos_start_a][self.pos_start_b])
    if self.counter % 2 == 0:
        self.tura = "czarne"
    if self.counter % 2 == 1:
        self.tura = "biale"

    if self.win == 0:
        print("Ruszają się: " + self.tura)
        if self.tura == "biale":
            if self.attacking[0] == "W":
                self.counter += 1
                print(self.counter, self.tura)
            else:
                print("Powinny sie ruszac biale!!")
                self.test()

        elif self.tura == "czarne":
            if self.attacking[0] == "B":
                self.counter += 1
                print(self.counter, self.tura)
            else:
                print("Powinny sie ruszac czarne!!")
                self.test()
        else:
            print("Zle dane")
            self.test()
