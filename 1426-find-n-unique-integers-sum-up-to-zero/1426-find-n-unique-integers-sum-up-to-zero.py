class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        # Add pairs (-i, i)
        for i in range(1, n // 2 + 1):
            result.append(-i)
            result.append(i)
        # If n is odd, include 0
        if n % 2 == 1:
            result.append(0)
        return result
        