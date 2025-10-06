class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, i, j)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        res = 0

        while min_heap:
            elevation, i, j = heapq.heappop(min_heap)
            res = max(res, elevation)
            if i == n - 1 and j == n - 1:
                return res
            if visited[i][j]:
                continue
            visited[i][j] = True

            for dx, dy in directions:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj]:
                    heapq.heappush(min_heap, (grid[ni][nj], ni, nj))
        