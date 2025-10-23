class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            next_s = ""
            for i in range(len(s) - 1):
                next_s += str((int(s[i]) + int(s[i + 1])) % 10)
            s = next_s
        return s[0] == s[1]
        