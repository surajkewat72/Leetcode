class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        original_profit = sum(strategy[i] * prices[i] for i in range(n))

        gain_first = [-(strategy[i] * prices[i]) for i in range(n)]
        gain_second = [(prices[i] - strategy[i] * prices[i]) for i in range(n)]

        half = k // 2

        pref_first = [0]
        pref_second = [0]

        for i in range(n):
            pref_first.append(pref_first[-1] + gain_first[i])
            pref_second.append(pref_second[-1] + gain_second[i])

        max_gain = 0

        for l in range(n - k + 1):
            mid = l + half
            r = l + k

            gain = (
                pref_first[mid] - pref_first[l] +
                pref_second[r] - pref_second[mid]
            )

            max_gain = max(max_gain, gain)

        return original_profit + max_gain
        