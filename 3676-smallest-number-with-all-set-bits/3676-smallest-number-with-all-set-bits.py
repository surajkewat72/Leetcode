class Solution:
    def smallestNumber(self, n: int) -> int:
        x = 1
        while x < n:
            x = x * 2 + 1
        return x
        # k = 1
        # while (1 << k) - 1 < n:
        #     k += 1
        # return (1 << k) - 1
        