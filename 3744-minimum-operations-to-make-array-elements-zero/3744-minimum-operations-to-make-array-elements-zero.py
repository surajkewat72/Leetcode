from typing import List

class Solution:
    @staticmethod
    def prefix(n: int) -> int:
        if n <= 0:
            return 0
        total = 0
        k = 1
        power = 1
        while True:
            next_power = power * 4
            if n < next_power:
                total += k * (n - power + 1)
                break
            total += k * (next_power - power)
            power = next_power
            k += 1
        return total

    def minOperations(self, queries: List[List[int]]) -> int:
        result = 0
        for l, r in queries:
            total_steps = Solution.prefix(r) - Solution.prefix(l - 1)
            result += (total_steps + 1) // 2 
        return result


        