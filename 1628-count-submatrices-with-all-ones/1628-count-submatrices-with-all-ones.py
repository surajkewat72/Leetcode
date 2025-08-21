class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        height = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    height[i][j] = 0
                else:
                    height[i][j] = height[i-1][j] + 1 if i > 0 else 1
        
        total = 0
        
        for i in range(m):
            for j in range(n):
                if height[i][j] > 0:
                    min_h = height[i][j]
                    for k in range(j, -1, -1):
                        if height[i][k] == 0:
                            break
                        min_h = min(min_h, height[i][k])
                        total += min_h
        return total
        