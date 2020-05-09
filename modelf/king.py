from modelf.importlibs import *
from modelf.abstraction import *
from modelf.collection import *


class King(PalyerMove, CollectionOfGame):
    def __init__(self, player :int, coord, time=5):
        self.player = player
        self.__coord = coord  # only len(coord) == 2
        self.__all_moves = [self.coord]
        self.time = time
        self.player1 = collections.defaultdict(list)
        self.player2 = collections.defaultdict(list)
        '''
        Structure of saving game : 
        {"Iteration : int, Player : int, Coords : list}
        '''
        CollectionOfGame.__init__(self, self.player1, self.player2)

    def __new__(cls, player, coord):
        if player != "black" and player != "white":
            raise Exception("Please write right player ! ")
        elif len(coord) != 2:
            raise Exception("Please cheak len coods !")
        else:
            print("WELCOME TO GAME ! ")
            return object.__new__(cls)

    def get_available_moves(self):
        # get all moves
        moves = list([(self.__coord[0] + 1, self.__coord[1] + 0),
                      (self.__coord[0] + 2, self.__coord[1] + 0),
                      (self.__coord[0] + 1, self.__coord[1] + 1),
                      (self.__coord[0] - 1, self.__coord[1] - 1)])
        return moves

    def cheak_move(self, move_to, all_moves):
        if move_to and len(move_to) == 2 and move_to in all_moves:
            return True
        else:
            return False

    def func_decorator_time(function):
        def wrapper(self, *args, **kwargs):
            start = timeit.timeit()
            function(self, *args, **kwargs)
            finish = timeit.timeit()
            if start - finish > self.time:
                raise Exception("You late !")
            else:
                print("Perfect time !")

        return wrapper

    @func_decorator_time
    def move(self, move_to=None, auto_move=False):
        if auto_move:
            self.coord = random.choice(self.get_available_moves())
        if self.cheak_move(move_to, self.get_available_moves()):
            self.__coord = move_to
            self.__all_moves.append(move_to)
        else:
            raise Exception("HELLO NOT RIGHT MOVE !")

    def set_coord(self, coord, iteration):
        self.__coord = coord
        super().save_result({"Iteration": iteration,  "Coords": coord, "Player":self.player}, self.player)

    def get_coord(self):
        return self.__coord

    def delete_coord(self):
        del self.__coord

    coord = property(get_coord, set_coord, delete_coord)
