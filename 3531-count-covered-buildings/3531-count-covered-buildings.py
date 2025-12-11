class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = defaultdict(list)
        cols = defaultdict(list)

        for x, y in buildings:
            rows[x].append(y)
            cols[y].append(x)

        for x in rows:
            rows[x].sort()
        for y in cols:
            cols[y].sort()

        covered = 0

        for x, y in buildings:
            row = rows[x]
            col = cols[y]

            i = bisect.bisect_left(row, y)
            has_left = i > 0
            has_right = i + 1 < len(row)

            j = bisect.bisect_left(col, x)
            has_above = j > 0
            has_below = j + 1 < len(col)

            if has_left and has_right and has_above and has_below:
                covered += 1

        return covered
        