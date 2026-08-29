class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.min_heap)
        heapq.heapify(self.max_heap)

    def addNum(self, num: int) -> None:
        if len(self.min_heap) and num>=self.min_heap[0]:
            heapq.heappush(self.min_heap, num)
            if len(self.min_heap)>len(self.max_heap): 
                heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
        else:
            heapq.heappush(self.max_heap, -1*num)
            if len(self.max_heap)>(len(self.min_heap)+1): 
                heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.min_heap)==len(self.max_heap): 
            return (-1*self.max_heap[0]+self.min_heap[0])/2
        return -1*self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()