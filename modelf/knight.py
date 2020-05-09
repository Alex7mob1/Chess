"""
module description
"""
import random
from itertools import product


class Knight:
    """This class models a behavior of knight chess figure"""
    bounds = (1, 8)

    def __init__(self, coord, player='white'):
        self._coord = coord  # coord = [x, y]
        self.player = player
        self.all_moves = [self._coord]

    @property
    def coord(self):
        return self._coord

    @coord.setter
    def coord(self, coord):
        '''
        if isinstance(coord, tuple) and len(coord) == 2 and self.bounds[0] <= coord[0] <= self.bounds[1] \
                and self.bounds[0] <= coord[1] <= self.bounds[1]:
            self._coord = coord
        else:
            raise Exception('Coordinates are incorrect')
        '''
        if coord[0]<=8 and coord[0]>=1 and coord[1]>=1 and coord[1]<=8:
            self._coord = coord
        else:
            raise Exception('Coordinates are incorrect')

    # coord = property(getCoord, setCoord)

    def get_available_moves(self):
        """"
            Method returns al available moves based on current position
        """
        # get all moves
        moves = list(product([self.coord[0] - 1, self.coord[0] + 1],
                             [self.coord[1] - 2, self.coord[1] + 2])) + \
                list(product([self.coord[0] - 2, self.coord[0] + 2],
                             [self.coord[1] - 1, self.coord[1] + 1]))
        # validate moves
        moves = [(x, y) for x, y in moves if self.bounds[1] >= x >= self.bounds[0] and
                 self.bounds[1] >= y >= self.bounds[0]]

        return moves

    def move(self, move_to=None, auto_move=False):
        all_moves = self.get_available_moves()
        # auto move is performed when auto_move variable is True
        if auto_move:
            self.coord = random.choice(all_moves)
            return
        # validate move_to defined by a user
        if move_to and len(move_to) == 2 and move_to in all_moves:
            self.coord = move_to
            self.all_moves.append(move_to)
        else:
            raise Exception('move_to parameter is incorrect. Try correct one')


