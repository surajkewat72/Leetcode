class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        used = set()
        result = 0
        current = -10**18  
        
        for x in nums:
            low, high = x - k, x + k
            candidate = max(current + 1, low)
            if candidate <= high:
                used.add(candidate)
                current = candidate
                result += 1
                
        return result
        