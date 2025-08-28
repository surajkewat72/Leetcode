class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        for i in range(k-1):
            nums.pop()
        return nums[-1]

    
