class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        
        ans = 0
        last1 = -10**18
        last2 = -10**18
        
        for l, r in intervals:
            if last2 < l:
                last1, last2 = r - 1, r
                ans += 2
            elif last1 < l <= last2:
                x = r if r != last2 else r - 1
                if x > last2:
                    last1, last2 = last2, x
                else:
                    last1 = x
                ans += 1

        return ans
