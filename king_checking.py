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
