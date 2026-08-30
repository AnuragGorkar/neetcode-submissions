class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = [[0 for j in range(n)] for i in range(m)]
        count[0][0] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    count[i][j] = 0
                else:
                    if i-1>=0:
                        count[i][j] += count[i-1][j]
                    if j-1>=0:
                        count[i][j] += count[i][j-1]
                    
        return count[m-1][n-1]
        