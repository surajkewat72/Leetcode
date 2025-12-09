class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        right = Counter(nums) 
        left = Counter()

        result = 0

        for j, val in enumerate(nums):
            right[val] -= 1  

            doubled = val * 2

            left_count = left[doubled]

            right_count = right[doubled]

            result = (result + left_count * right_count) % MOD

            left[val] += 1

        return result