class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        
        for num in nums:
            stack.append(num)
            
            while len(stack) > 1:
                x, y = stack[-2], stack[-1]
                g = math.gcd(x, y)
                if g > 1:  
                    lcm = x * y // g
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        
        return stack
        