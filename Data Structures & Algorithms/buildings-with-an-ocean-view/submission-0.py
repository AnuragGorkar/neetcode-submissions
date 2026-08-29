class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        suffix_max = 0
        res = []
        for i in range(n-1, -1, -1):
            if heights[i] > suffix_max:
                res.append(i)
                suffix_max = heights[i]
        return res[::-1]
             
        