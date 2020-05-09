from modelf.importlibs import  *

class BoardRules(ABC):
    def __init__(self, size_of_borad =[8, 8]):
        self.size_of_borad = size_of_borad
        self.board = self.create_board()
        self.len_pawn = 8

    def create_board(self):
        return {"X": [i for i in range(self.size_of_borad[0])],
                "Y": [i for i in range(self.size_of_borad[0])]}

    def init_positions_pawns(self):
        print(self.create_board())
        pawns = collections.defaultdict(list)
        for i in range(self.len_pawn):
            pawns['pawns-'+str(i)].append({"X": self.board['X'][i], "Y": self.board['Y'][3]})
        return dict(pawns)

    @staticmethod
    def func_decorator_cheak(function):
        def wrapper(self):
            right_movies = []
            for i, batch in enumerate(function(self)):
                if not batch[0] >= self.size_of_borad[0] or \
                        not batch[1] >= self.size_of_borad[1] :
                    right_movies.append((batch))
            return right_movies
        return wrapper



# board_object = BoardRules()
# board_object.init_positions()
