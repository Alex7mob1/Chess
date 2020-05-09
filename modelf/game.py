from modelf.importlibs import *
from modelf.pawns import Pawn
from modelf.king import King

PLAYER = ['white', 'black']
name_of_figure = "pawns-1"

player1Pawn = Pawn(player=PLAYER[0], coord=(0, 2), name_of_figure=name_of_figure)
player2Pawn = Pawn(player=PLAYER[1], coord=(0, 2), name_of_figure=name_of_figure)

player1Pawn.move(1, auto_move=True)
player1Pawn.move(2, auto_move=True)
player1Pawn.move(3, auto_move=True)

print("all movies of white  player :  ", player1Pawn.coord)

player2Pawn.move(1, auto_move=True)
player2Pawn.move(2, auto_move=True)
# player2Pawn.move(3, auto_move=True)

print(player2Pawn.coord)

