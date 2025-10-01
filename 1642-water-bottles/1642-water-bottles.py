class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty = numBottles
        
        while empty >= numExchange:
            new_full = empty // numExchange
            total_drunk += new_full
            empty = empty - new_full * numExchange + new_full
            
        return total_drunk

        