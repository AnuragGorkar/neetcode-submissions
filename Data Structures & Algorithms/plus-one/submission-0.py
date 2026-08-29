class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s, c = 0, 1
        res = []
        for dig in digits[::-1]: 
            c, s = (dig + c)//10, (dig + c)%10
            res.append(s)
        if c:
            res.append(c)
        return res[::-1]
        