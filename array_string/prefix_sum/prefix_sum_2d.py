# constucting 2d prefix sum of a range
# zero padded prefix sum range of (m+1)(n+1)
# Construction Logic
# Prefix sum of every value above, every value left, then removing the double counted top left corner cell
def construct_2d_prefix_sum(matrix: list[list[int]]) -> list[list[int]]:
    m = len(matrix)
    n = len(matrix[0])
    prefix_sum = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            prefix_sum[i + 1][j + 1] = (
                matrix[i][j]
                + prefix_sum[i][j + 1]
                + prefix_sum[i + 1][j]
                - prefix_sum[i][j]
            )

    return prefix_sum


# query of prefix sum
# get sum from 0,0 to r2,c2
# subtract everything to the left (r2 c1)
# subtract everything to the top (r1 c2)
# add back double subtracted top left cell (r1 c1)
def query_2d_prefix_sum(
    prefix_sum: list[list[int]], r1: int, c1: int, r2: int, c2: int
) -> int:
    return (
        prefix_sum[r2 + 1][c2 + 1]
        - prefix_sum[r2 + 1][c1]
        - prefix_sum[r1][c2 + 1]
        + prefix_sum[r1][c1]
    )
