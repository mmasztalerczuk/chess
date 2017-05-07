def checking(self):
    # *** BLACK KING ***
    # *** check by black pawn
    if (self.bking_a - 1 and self.bking_b + 1) or (self.bking_a - 1 and self.bking_b - 1) == self.wpawn:
        print("Dupa")

    # *** check black knight ***
    try:
        if (self.bking_a + 2 and self.bking_b + 1) or (self.bking_a + 2 and self.bking_b - 1) \
                or (self.bking_a - 2 and self.bking_b + 1) or (self.bking_a - 2 and self.bking_b - 1) \
                or (self.bking_a + 1 and self.bking_b + 2) or (self.bking_a + 1 and self.bking_b - 2) \
                or (self.bking_a - 1 and self.bking_b + 2) \
                or (self.bking_a - 1 and self.bking_b - 2) == self.wknight:
            print("szach koń - bialy krol")
    except IndexError:
        print("szach bialy kon krawedz")