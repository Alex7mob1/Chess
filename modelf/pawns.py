from modelf.importlibs import *
from modelf.abstraction import *
from modelf.collection import *
from board import *

from modelf.abstraction import PalyerMove
from modelf.collection import CollectionOfGame


class Pawn(PalyerMove, CollectionOfGame, BoardRules):
    def __init__(self, player: str, coord, name_of_figure, time=5):
        self.player = player
        self.__coord = coord  # only len(coord) == 2
        self.name_of_figure = name_of_figure
        self.time = time
        self.player1 = collections.defaultdict(list)
        self.player2 = collections.defaultdict(list)
        '''
        Structure of saving game : 
        {"iteration : int, Player : str, coord : list}
        '''
        CollectionOfGame.__init__(self, self.player1, self.player2)
        BoardRules.__init__(self)
        super().save_result(
            {"Iteration": 0, "Coords": None, "Player": self.player, "name_figure": self.name_of_figure, \
             "Position": super().init_positions_pawns()[self.name_of_figure]}, self.player)


    def __new__(cls, player, coord, name_of_figure):
        if player != "black" and player != "white":
            raise Exception("Please write right player ! ")
        elif len(coord) != 2:
            raise Exception("Please cheak len coods !")
        else:
            print("WELCOME TO GAME ! ")
            return object.__new__(cls)

    @BoardRules.func_decorator_cheak
    def get_available_moves(self):
        # get all moves
        all_moves = [(self.__coord[0] + 1, self.__coord[1] + 0), (self.__coord[0] + 3, self.__coord[1] + 0)]
        return all_moves

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
    def move(self, iteration, move_to=None, auto_move=False):
        if auto_move:
            self.coord = [iteration, random.choice(self.get_available_moves())]
            super().save_result({"Iteration": iteration, "Coords": self.__coord, "Player": self.player}, self.player)
        if self.cheak_move(move_to, self.get_available_moves()):
            self.coord = move_to
            super().save_result({"Iteration": iteration, "Coords": self.__coord, "Player": self.player}, self.player)
        else:
            pass
            #raise Exception("HELLO NOT RIGHT MOVE !")

    def set_coord(self, args): #coord, iteration: int, name_of_figure):
        self.__coord = args[1]
        print(args[0])
        print("\n"*3)
        old_position = self.coord[args[0]-1][0]['Position'][0]
        print(old_position["Y"])
        print("\n"*3)
        super().save_result({"Iteration": args[0],  "Coords": args[1], "Player": self.player, \
                             "Position":[{"X":old_position["X"] + args[1][0],"Y":old_position["Y"] + args[1][1]}]}, self.player)
        # super().save_result({"Iteration": args[0],  "Coords": args[1], "Player": self.player}, self.player)

    def get_coord(self):
        return super().get_info_moves(self.player)

    def delete_coord(self):
        del self.__coord

    coord = property(get_coord, set_coord, delete_coord)

# PLAYER = ['white', 'black']
# coord = (1, 2)
#
# pawn_object = pawn(PLAYER[0], coord)
#
# print(pawn_object.coord)
# #
#
# move = pawn_object.get_available_moves()
#
# print(move)
# print(type(move))
#
# pawn_object.move(move_to=(2, 2))
