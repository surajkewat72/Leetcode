class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        inc = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                inc[i] = inc[i - 1] + 1

        dec = [1] * n
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                dec[i] = dec[i + 1] + 1

        max_k = 0
        for i in range(n - 1):
            k = min(inc[i], dec[i + 1])
            max_k = max(max_k, k)

        return max_k
        