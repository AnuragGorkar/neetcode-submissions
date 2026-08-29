class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        points = [(-math.sqrt(point[0]**2+point[1]**2), point[0], point[1]) for point in points]
        heapq.heapify(points)
        while len(points)>k: 
            heapq.heappop(points)
        points = [[point[1], point[2]] for point in points]
        return points
        