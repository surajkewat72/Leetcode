class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag_sq = -1
        best_area = -1
        
        for length, width in dimensions:
            diag_sq = length * length + width * width
            area = length * width
            
            if diag_sq > max_diag_sq:
                max_diag_sq = diag_sq
                best_area = area
            elif diag_sq == max_diag_sq:
                best_area = max(best_area, area)
        
        return best_area
        