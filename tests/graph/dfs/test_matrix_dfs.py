import unittest
from graph.dfs.matrix_dfs import exist


def test_matrix_dfs():
    board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    assert exist(board1, "ABCCED") == True
    assert exist(board1, "SEE") == True
    assert exist(board1, "ABCB") == False
    board2 = [["a"]]
    assert exist(board2, "a") == True
    assert exist(board2, "b") == False
    print("All Matrix DFS tests passed!")
