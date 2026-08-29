class Solution:
    def climbStairs(self, n: int) -> int:
        curr, prev = 1, 1
        for _ in range(n-1): 
            prev, curr  = curr, curr+prev
        return curr
        
        