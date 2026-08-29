class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperatures = [(temp, index) for index, temp in enumerate(temperatures)]
        
        nge = deque()
        res = [0] * len(temperatures)
        for temp, index in temperatures[::-1]: 
            if not len(nge): 
                res[index] = 0
            else:
                while len(nge) and nge[-1][0]<=temp:
                    nge.pop()
                if len(nge): 
                    res[index] = nge[-1][1] - index
                else: 
                    res[index] = 0
            nge.append((temp, index))
                
        return res