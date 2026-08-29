class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        heapq.heapify(minheap)
        for num in nums: 
            heapq.heappush(minheap, num)
            if len(minheap)>k:
                heapq.heappop(minheap) 
        return minheap[0] 