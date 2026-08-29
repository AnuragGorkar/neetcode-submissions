class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_rev = [-1*x for x in stones]
        heapq.heapify(stones_rev)
        while len(stones_rev)>1: 
            largest = heapq.heappop(stones_rev)
            second_largest = heapq.heappop(stones_rev)
            if largest-second_largest:
                heapq.heappush(stones_rev, largest-second_largest)
        if not len(stones_rev): 
            return 0
        return -1*stones_rev[0] 