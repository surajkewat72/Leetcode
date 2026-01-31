class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        flag=False
        for i in letters:
            if ord(i)>ord(target):
                flag=True
                return i
        if flag==False:
            return letters[0]
        