class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        mp = defaultdict(list)
        for a, b, c in allowed:
            mp[(a, b)].append(c)
        
        memo = {}

        def dfs(curr):
            if len(curr) == 1:
                return True
            
            if curr in memo:
                return memo[curr]
            
            def backtrack(i, path):
                if i == len(curr) - 1:
                    return dfs("".join(path))
                
                pair = (curr[i], curr[i+1])
                if pair not in mp:
                    return False
                
                for ch in mp[pair]:
                    path.append(ch)
                    if backtrack(i + 1, path):
                        return True
                    path.pop()
                
                return False
            
            memo[curr] = backtrack(0, [])
            return memo[curr]
        
        return dfs(bottom)
        