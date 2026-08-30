class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m, n = len(points), len(points[0])
        maxPoints = [[0 for j in range(n)] for i in range(m)]

        maxPoints[0][:] = points[0][:]

        for i in range(1, m):
            for j in range(n):
                max_in_row = -sys.maxsize
                for k in range(n):
                    max_in_row = max(max_in_row, points[i][j]+maxPoints[i-1][k]-abs(k-j))
                maxPoints[i][j] = max_in_row
        
        return max(maxPoints[-1][:])