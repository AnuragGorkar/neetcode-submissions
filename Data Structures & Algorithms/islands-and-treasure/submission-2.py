class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n =  len(grid), len(grid[0])
        di_dj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        INF = 2147483647;

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 0: 
                    bfs_queue = deque()
                    bfs_queue.append((i, j, 0))

                    while len(bfs_queue): 
                        i, j, depth = bfs_queue.popleft()
                        grid[i][j] = depth
                        for di, dj in di_dj: 
                            ni = i + di
                            nj = j + dj
                            if ni>=0 and nj>=0 and ni<m and nj<n and grid[ni][nj] != -1 and grid[ni][nj] != -2 and grid[ni][nj] > (depth+1): 
                                grid[ni][nj] = -2
                                bfs_queue.append((ni, nj, depth+1))