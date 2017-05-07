from messages import *


# function checking if destined position isn't already taken by figure of the same color
def attack(self):
    a = self.pos_start_a
    b = self.pos_start_b
    a1 = self.pos_end_a
    b1 = self.pos_end_b
    self.attacking = list(self.board[a][b])
    self.attacked = list(self.board[a1][b1])
    if self.attacking[0] == self.attacked[0]:
        error_wrong_square(self)