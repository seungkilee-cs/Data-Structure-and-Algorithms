import unittest
from graph.dfs.matrix_dfs_recursive import exist


class TestMatrixDFS(unittest.TestCase):
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    board2 = [["a"]]
    print(f"board1: {board1}")
    print(f"board2: {board2}")

    def test_board1(self):
        board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
        print(f"board1: {board1}")
        self.assertTrue(exist(board1, "ABCCED"))
        self.assertTrue(exist(board1, "SEE"))
        self.assertFalse(exist(board1, "ABCB"))

    def test_board2(self):
        board2 = [["a"]]
        print(f"board2: {board2}")
        self.assertTrue(exist(board2, "a"))
        self.assertFalse(exist(board2, "b"))


if __name__ == "__main__":
    unittest.main()
