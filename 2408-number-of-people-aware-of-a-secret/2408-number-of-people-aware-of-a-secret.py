class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1  
        
        for day in range(1, n + 1):
            if dp[day] == 0: 
                continue

            for share_day in range(day + delay, min(n + 1, day + forget)):
                dp[share_day] = (dp[share_day] + dp[day]) % MOD
        
  
        ans = 0
        for day in range(n - forget + 1, n + 1):
            ans = (ans + dp[day]) % MOD
        return ans
        