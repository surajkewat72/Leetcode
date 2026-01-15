class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def longest_consecutive(arr):
            arr.sort()
            best = cur = 1
            
            for i in range(1, len(arr)):
                if arr[i] == arr[i-1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            
            return best

        maxH = longest_consecutive(hBars) + 1
        maxV = longest_consecutive(vBars) + 1

        side = min(maxH, maxV)
        return side * side
        