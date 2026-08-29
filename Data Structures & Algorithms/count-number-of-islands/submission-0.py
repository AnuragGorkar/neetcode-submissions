class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j, visited):
            if i<0 or j<0 or i==m or j==n or visited[i][j] or grid[i][j] == "0": 
                return
            else: 
                grid[i][j] = "0"
                visited[i][j] = "1"
                dfs(i+1, j, visited)
                dfs(i, j+1, visited)
                dfs(i-1, j, visited)
                dfs(i, j-1, visited)

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1": 
                    count += 1
                    visited = [[0]*n for _ in range(m)]
                    dfs(i, j, visited)
        
        return count