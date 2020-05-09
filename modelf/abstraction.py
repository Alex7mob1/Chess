from modelf.importlibs import *


class PalyerMove(ABC):

    @abstractmethod
    def get_available_moves(self) -> list:
        pass

    @abstractmethod
    def move(self, move_to=None, auto_move=False) -> list:
        pass
