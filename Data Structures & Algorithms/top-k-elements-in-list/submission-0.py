class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        
        for num in nums:
            freq[num] = freq.setdefault(num, 0) + 1
        
        min_heap = [] 
        heapq.heapify(min_heap)

        for key, value in freq.items():
            heapq.heappush(min_heap, (value, key))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        res = []
        while len(min_heap):
            res.append(heapq.heappop(min_heap)[1])
        return res