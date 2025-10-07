class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        n = len(rains)
        ans = [-1] * n
        full = {}       
        dry_days = []     
        
        for i, lake in enumerate(rains):
            if lake == 0:
                dry_days.append(i)
            else:
                if lake in full:
                    last_rain = full[lake]
                    idx = bisect.bisect_right(dry_days, last_rain)
                    
                    if idx == len(dry_days):
                        return []  
                    
                    dry_day = dry_days[idx]
                    ans[dry_day] = lake 
                    dry_days.pop(idx)    
                
    
                full[lake] = i

        for d in dry_days:
            ans[d] = 1
        
        return ans
        