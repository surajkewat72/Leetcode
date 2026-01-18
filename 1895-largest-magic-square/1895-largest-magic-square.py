class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        row = [[0] * (n + 1) for _ in range(m)]
        col = [[0] * n for _ in range(m + 1)]
        diag1 = [[0] * (n + 1) for _ in range(m + 1)]
        diag2 = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                row[i][j + 1] = row[i][j] + grid[i][j]
                col[i + 1][j] = col[i][j] + grid[i][j]
                diag1[i + 1][j + 1] = diag1[i][j] + grid[i][j]
                diag2[i + 1][j] = diag2[i][j + 1] + grid[i][j]

        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):

                    target = row[i][j + k] - row[i][j]

                    if any(row[i + x][j + k] - row[i + x][j] != target for x in range(k)):
                        continue

                    if any(col[i + k][j + x] - col[i][j + x] != target for x in range(k)):
                        continue

                    if diag1[i + k][j + k] - diag1[i][j] != target:
                        continue

                    if diag2[i + k][j] - diag2[i][j + k] != target:
                        continue

                    return k

        return 1
        