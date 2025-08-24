class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        pre=0
        curr=0
        ans=0
        for i in nums:
            if i==1:
                curr+=1
            else:
                ans=max(ans,pre+curr)
                pre=curr
                curr=0
                
        ans=max(ans,pre+curr)
        if ans==len(nums):
            return (len(nums)-1)
        else:
            return ans
        