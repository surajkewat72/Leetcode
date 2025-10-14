class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
    
        def isIncreasing(start):
            for i in range(start, start + k - 1):
                if nums[i] >= nums[i + 1]:
                    return False
            return True
        
        for a in range(n - 2 * k + 1):
            if isIncreasing(a) and isIncreasing(a + k):
                return True
        
        return False
        