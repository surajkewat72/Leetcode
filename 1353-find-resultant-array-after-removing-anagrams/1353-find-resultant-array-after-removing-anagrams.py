class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def isAnagram(a, b):
            return sorted(a) == sorted(b)
        
        stack = []
        for word in words:
            if stack and isAnagram(stack[-1], word):
                continue 
            stack.append(word)
        return stack
        