class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        empty = numBottles

        while empty >= numExchange:
            empty -= numExchange    
            numExchange += 1         
            drank += 1               
            empty += 1              

        return drank

        