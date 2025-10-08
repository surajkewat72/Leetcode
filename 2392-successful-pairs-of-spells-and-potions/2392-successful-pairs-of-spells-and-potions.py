class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        n = len(potions)
        result = []
        
        for s in spells:
            target = (success + s - 1) // s  
            idx = bisect_left(potions, target)
            result.append(n - idx)
        
        return result
        