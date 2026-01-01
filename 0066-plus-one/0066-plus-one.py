class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=int("".join(map(str,digits)))
        st=str(num+1)
        return list(map(int,st))
        