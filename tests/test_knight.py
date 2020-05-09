import unittest
from modelf.knight import Knight


class TestKnight(unittest.TestCase):

    def test_moves(self):

        k = Knight(coord=[1, 2])
        k.move(auto_move=True)
        available_moves = ((3, 3), (3, 1), (2, 4))
        self.assertTrue(available_moves.__contains__(k.coord))

        k = Knight(coord=[3, 3])
        k.move(auto_move=True)
        available_moves = ((1, 4), (5, 4), (2, 5), (4, 5), (1, 2), (2, 1), (4, 1), (5, 2))
        self.assertTrue(available_moves.__contains__(k.coord))



    def test_coord(self):
        k = Knight(coord=[1, 2])

        with self.assertRaises(Exception):
            k.coord = [2, 9]

        with self.assertRaises(Exception):
            k.coord = [0, 7]

        with self.assertRaises(Exception):
            k.coord = [9, 2]

        with self.assertRaises(Exception):
            k.coord = [7, 0]

        k.coord = [2, 7]
        self.assertEqual(k.coord, [2, 7])

    def test_get_available_moves(self):

        k = Knight(coord=[1, 2])
        available_moves = [(3, 3), (3, 1), (2, 4)]
        self.assertCountEqual(k.get_available_moves(), available_moves)

        k = Knight(coord=[3, 3])
        available_moves = [(1, 4), (5, 4), (2, 5), (4, 5), (1, 2), (2, 1), (4, 1), (5, 2)]
        self.assertCountEqual(k.get_available_moves(), available_moves)


if __name__ == '__main__':
    unittest.main()
