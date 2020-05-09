import random

class Rook:
    bounds = (1, 8)

    # ID = 0
    def __init__(self, coords=None, player="white"):
        self.coords = coords  # atributs
        self.pleyer = player
        self.all_moves = [self.coords]

    def get_available_moves(self):
        moves = []


        return moves

    def move(self, move_to=None, auto_move=False):
        all_moves = self.get_available_moves()
        if auto_move:
            self.coords = random.choice(all_moves)
            return
        if move_to and len(move_to) == 2 and move_to in all_moves:
            self.coords = move_to
            self.all_moves.append(move_to)
        else:
            raise Exception("eror")


k = Rook(coords=[1, 1])
k.move(auto_move=True)
print(k.coords)