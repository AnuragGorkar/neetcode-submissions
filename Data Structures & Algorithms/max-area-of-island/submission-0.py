class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_size = 0
        for i in range(m): 
            for j in range(n): 
                if grid[i][j]: 
                    size = 0
                    grid[i][j] = 0
                    bfs_queue = deque()
                    bfs_queue.append((i, j))

                    while len(bfs_queue): 
                        size += 1
                        x, y = bfs_queue[0]
                        bfs_queue.popleft()

                        dx_dy = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                        for dx, dy in dx_dy: 
                            new_x = x + dx
                            new_y = y + dy
                            if new_x>=0 and new_y>=0 and new_x<m and new_y<n and grid[new_x][new_y]:
                                grid[new_x][new_y] = 0 
                                bfs_queue.append((new_x, new_y))
                    
                    max_size = max(size, max_size)
        return max_size