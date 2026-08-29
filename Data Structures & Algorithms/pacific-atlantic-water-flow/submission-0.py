class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific_set = set()
        atlantic_set = set()
        di_dj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        # , [1, 1], [-1, -1], [-1, 1], [1, -1]]

        def dfs(i, j, reached_set, visited):
            reached_set.add((i, j))
            for di, dj in di_dj:
                ni, nj = i+di, j+dj
                if ni>=0 and ni<m and nj>=0 and nj<n and (not visited[ni][nj]) and heights[ni][nj] >= heights[i][j]:
                    visited[ni][nj] = True
                    dfs(ni, nj, reached_set, visited)

        for j in range(n):
            visited = [[False]*n for _ in range(m)]  
            dfs(0, j, pacific_set, visited)
        
        for i in range(m):
            visited = [[False]*n for _ in range(m)]  
            dfs(i, 0, pacific_set, visited)

        for j in range(n):
            visited = [[False]*n for _ in range(m)]  
            dfs(m-1, j, atlantic_set, visited)
        
        for i in range(m-1):
            visited = [[False]*n for _ in range(m)]  
            dfs(i, n-1, atlantic_set, visited)

        return list(pacific_set & atlantic_set)