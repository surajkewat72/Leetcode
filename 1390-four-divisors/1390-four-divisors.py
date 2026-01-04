class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
    
        for x in nums:
            divisors = set()
            i = 1
            
            while i * i <= x:
                if x % i == 0:
                    divisors.add(i)
                    divisors.add(x // i)
                    if len(divisors) > 4:
                        break
                i += 1
            
            if len(divisors) == 4:
                total += sum(divisors)
        
        return total
        