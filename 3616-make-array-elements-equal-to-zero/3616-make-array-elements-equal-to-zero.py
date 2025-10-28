class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        
        def simulate(start, direction):
            arr = nums[:]
            curr = start
            d = direction
            while 0 <= curr < n:
                if arr[curr] == 0:
                    curr += d
                else:
                    arr[curr] -= 1
                    d *= -1
                    curr += d
            return all(x == 0 for x in arr)
        
        valid = 0
        for i in range(n):
            if nums[i] == 0:
                if simulate(i, 1):  
                    valid += 1
                if simulate(i, -1):  
                    valid += 1
        return valid

        