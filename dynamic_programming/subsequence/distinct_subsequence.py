def distinct_subsequence(s: str, t: str) -> int:
    if len(s) < len(t):
        return 0

    # Set up
    m, n = len(s), len(t)
    cache = [[0] * (n + 1) for _ in range(m + 1)]
    # Base Case - empty string t
    for i in range(len(s) + 1):
        cache[i][0] = 1
    # Build Other Cases
    # Character Match
    # use
    # skip
    # Character Doesn't Match -> Skip
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            cache[i][j] = (
                cache[i - 1][j - 1] + cache[i - 1][j]
                if s[i - 1] == t[j - 1]
                else cache[i - 1][j]
            )
    return cache[len(s)][len(t)]
