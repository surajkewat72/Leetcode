class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        nl=[]
        for i in nums:
            if nums.count(i)==2:
                nl.append(i)
                nums.remove(i)
                nums.remove(i)
        return nl
        