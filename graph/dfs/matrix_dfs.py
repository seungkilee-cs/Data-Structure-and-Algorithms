def exist(matrix: list[list[str]], word: str) -> bool:
    print(f"Word To Search: {word}")
    if not matrix or not matrix[0]:
        return False
    m, n = len(matrix), len(matrix[0])
    visited = [[False] * n for _ in range(m)]

    def dfs(r: int, c: int, idx: int) -> bool:
        # base case
        if len(word) == idx:
            return True
        # recursive case
        # Validate index, visited, value
        if (
            0 > r
            or r >= m
            or 0 > c
            or c >= n
            or visited[r][c]
            or matrix[r][c] != word[idx]
        ):
            return False
        visited[r][c] = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            rp, cp = r + dr, c + dc
            if dfs(r=rp, c=cp, idx=idx + 1):
                return True
        # backtrack
        visited[r][c] = False
        # return false if we cannot find the word
        return False

    for i in range(m):
        for j in range(n):
            if dfs(r=i, c=j, idx=0):
                print("True")
                return True
    print("False")
    return False
