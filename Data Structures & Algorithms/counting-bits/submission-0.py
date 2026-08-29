class Solution:
    def countBits(self, n: int) -> List[int]:
        def getBitCount(num): 
            count = 0
            for i in range(32): 
                if (num>>i)&1: 
                    count+=1
            return count

        res = [0]*(n+1)
        for i in range(n+1): 
            res[i] = getBitCount(i)
            
        return res
        