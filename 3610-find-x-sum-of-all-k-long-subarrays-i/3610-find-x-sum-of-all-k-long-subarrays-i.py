class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            freq = Counter(sub)
            
            top = sorted(freq.items(), key=lambda a: (a[1], a[0]), reverse=True)
            chosen = [num for num, _ in top[:x]]            
            total = sum(num for num in sub if num in chosen)
            ans.append(total)
        
        return ans
        