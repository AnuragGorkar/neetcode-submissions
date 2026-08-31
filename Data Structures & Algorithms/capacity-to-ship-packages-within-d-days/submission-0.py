class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        low, high = max(weights), sum(weights)


        def possible(weight):
            count = 1
            curr_weight = 0
            for w in weights:
                if curr_weight+w<=weight:
                    curr_weight += w
                else:
                    curr_weight = w
                    count += 1

            return count<=days

        while low<=high:
            mid = (low+high)//2
            if possible(mid):
                high = mid-1
            else:
                low = mid+1
                
        
        return low
        