class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for query in queries: 
            minLength = sys.maxsize
            for interval in intervals:
                if query>=interval[0] and  query<=interval[1]: 
                    minLength = min(minLength, interval[1]-interval[0]+1)
            if minLength == sys.maxsize: 
                minLength = -1
            res.append(minLength)
        return res
        