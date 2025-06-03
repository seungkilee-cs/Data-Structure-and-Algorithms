def sweep_line(intervals: list[list[int]], queries: list[int]) -> list[int]:
    res = []
    intervals.sort()
    queries_index_mapping = sorted([(v, i) for i, v in enumerate(queries)])
    res = [0] * len(queries)
    i = 0

    for q, j in queries_index_mapping:
        while i < len(intervals) and intervals[i][0] <= q and intervals[i][1] >= q:
            start, end = intervals[i]
            res[j] = start - end
            i += 1

    return res
