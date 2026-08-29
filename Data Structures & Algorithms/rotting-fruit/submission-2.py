class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        di_dj = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        time = 0
        bfs_queue = deque()

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == 2:
                    bfs_queue.append((i, j))

        if len(bfs_queue):
            time = -1
        while len(bfs_queue):
            time += 1
            bfs_queue_length = len(bfs_queue)
            for _ in range(bfs_queue_length):
                i, j = bfs_queue.popleft()
                for di, dj in di_dj: 
                    ni, nj = i+di, j+dj
                    if ni>=0 and nj>=0 and ni<m and nj<n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        bfs_queue.append((ni, nj))

        for i in range(m): 
            for j in range(n):
                if grid[i][j] == 1: 
                    return -1

        return time
        