class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        
        n = len(events)
        
        maxSuffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            maxSuffix[i] = max(maxSuffix[i + 1], events[i][2])
        
        starts = [e[0] for e in events]
        
        ans = 0
        
        for i in range(n):
            start, end, val = events[i]
            
            ans = max(ans, val)
            
            j = bisect.bisect_left(starts, end + 1)
            if j < n:
                ans = max(ans, val + maxSuffix[j])
        
        return ans
        