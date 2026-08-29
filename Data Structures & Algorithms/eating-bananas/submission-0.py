class Solution:
    def hoursTaken(self, piles, k):
        time = 0
        for i in range(len(piles)): 
            time += math.ceil(piles[i]/k)
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_bananas = max(piles)
        low, high = 1, max_bananas
        while low<=high: 
            mid = (low + high)//2
            if self.hoursTaken(piles, mid)<=h:
                high = mid-1
            else: 
                low = mid+1
        return low
        