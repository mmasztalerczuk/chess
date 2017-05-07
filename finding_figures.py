# *** BLACK KING ****
def find_bking(self):
    # *** BLACK KING ***
    for figure_iter1 in self.board:
        self.bking_b = 0
        for figure_iter2 in figure_iter1:
            if figure_iter2 == 'BK ':
                return self.bking_a, self.bking_b
            self.bking_b += 1
        self.bking_a += 1


# *** WHITE KING ***
def find_wking(self):
    # *** WHITE KING ***
    for figure_iter1 in self.board:
        self.wking_b = 0
        for figure_iter2 in figure_iter1:
            if figure_iter2 == 'WK ':
                return self.wking_a, self.wking_b
            self.wking_b += 1
        self.bking_a += 1


# *** BLACK ROOK ***
def find_brook(self):
    self.brook_a = 0
    for figure_iter3 in self.board:
        self.brook_b = 0
        for figure_iter4 in figure_iter3:
            if figure_iter4 == 'BR ':
                return self.brook_a, self.brook_b
            self.brook_b += 1
        self.brook_a += 1