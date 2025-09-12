class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = set("aeiou")
        total_vowels = sum(1 for ch in s if ch in vowels)
        return total_vowels > 0