class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        count = [[grid[i][j] for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if not i and not j:
                    continue
                top, left = sys.maxsize, sys.maxsize
                if i-1>=0:
                    top = count[i-1][j]
                if j-1>=0:
                    left = count[i][j-1]
                count[i][j] += min(top, left)
        
        print(count)
                    
        return count[m-1][n-1]
        