class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0
        streak = 0

        for i in range(len(prices)):
            if i > 0 and prices[i - 1] - prices[i] == 1:
                streak += 1
            else:
                streak = 1
            ans += streak

        return ans
            