def exist(matrix: list[list[str]], word: str) -> bool:
    m, n = len(matrix), len(matrix[0])

    def dfs(r: int, c: int, idx: int) -> bool:
        return False

    for i in range(m):
        for j in range(n):
            if dfs(r=i, c=j, idx=0):
                return True
    return False
