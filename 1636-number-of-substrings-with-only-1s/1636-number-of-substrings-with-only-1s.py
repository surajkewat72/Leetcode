class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        count = 0
        result = 0
        
        for ch in s:
            if ch == '1':
                count += 1
            else:
                result = (result + count * (count + 1) // 2) % MOD
                count = 0
        
        if count > 0:
            result = (result + count * (count + 1) // 2) % MOD

        return result

        