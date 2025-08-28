class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = {}

        for i in range(n):
            for j in range(n):
                key = i - j
                if key not in diagonals:
                    diagonals[key] = []
                diagonals[key].append(grid[i][j])

        for key, vals in diagonals.items():
            if key >= 0: 
                vals.sort(reverse=True) 
            else: 
                vals.sort()  
            diagonals[key] = vals

        for i in range(n):
            for j in range(n):
                key = i - j
                grid[i][j] = diagonals[key].pop(0)

        return grid
        