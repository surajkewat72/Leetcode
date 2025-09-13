class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = set("aeiou")
    
        vowel_freq = {}
        consonant_freq = {}
        
        for ch in s:
            if ch in vowels:
                vowel_freq[ch] = vowel_freq.get(ch, 0) + 1
            else:
                consonant_freq[ch] = consonant_freq.get(ch, 0) + 1
        
        max_vowel = max(vowel_freq.values(), default=0)
        max_consonant = max(consonant_freq.values(), default=0)
        
        return max_vowel + max_consonant
        