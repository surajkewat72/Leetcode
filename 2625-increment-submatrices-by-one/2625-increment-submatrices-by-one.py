class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        diff = [[0] * (n+1) for _ in range(n+1)]

        for r1, c1, r2, c2 in queries:
            diff[r1][c1] += 1
            diff[r1][c2+1] -= 1
            diff[r2+1][c1] -= 1
            diff[r2+1][c2+1] += 1

        mat = [[0]*n for _ in range(n)]
        for i in range(n):
            curr = 0
            for j in range(n):
                curr += diff[i][j]
                diff[i][j] = curr

        for j in range(n):
            curr = 0
            for i in range(n):
                curr += diff[i][j]
                mat[i][j] = curr

        return mat
        