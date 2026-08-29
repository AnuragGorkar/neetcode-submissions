class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        curr, prev = 2, 1
        n-=2
        while n: 
            prev, curr  = curr, curr+prev
            n-=1
        return curr
        
        