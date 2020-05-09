from modelf.importlibs import *


class CollectionOfGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_info_palyer_1(self):
        return dict(self.player1)

    def get_info_palyer_2(self):
        return dict(self.player2)

    def save_result(self, info_of_move:dict, player:str) -> None:
        if player == "white": self.player1[info_of_move['Iteration']].append(info_of_move)
        elif player == "black": self.player2[info_of_move['Iteration']].append(info_of_move)
        else : raise Exception("What is it ?")

    def get_info_moves(self, player):
        if player == "white":
            return self.get_info_palyer_1()
        elif player == "black":
            return self.get_info_palyer_2()
        else:
            raise Exception("Not right player")

# player1 = collections.defaultdict(list)
# player2 = collections.defaultdict(list)
#
# game = CollectionOfGame(player1, player2)
# game.save_result({"Iteration": 1, "name": "Ostap"}, 'white')
# game.save_result({"Iteration": 2, "name": "Ostap"}, 'white')
# game.save_result({"Iteration": 3, "name": "Ostap"}, 'white')
# print(game.get_info_moves("white"))
#
# game.save_result({"Iteration": 1, "name": "Max"}, 'black')
# game.save_result({"Iteration": 2, "name": "Max"}, 'black')
# game.save_result({"Iteration": 3, "name": "Max"}, 'black')
# print(game.get_info_moves("black"))

