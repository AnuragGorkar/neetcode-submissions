class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0

        for i in range(m): 
            for j in range(n): 
                if grid[i][j] == "1":
                    count += 1 
                    bfs_queue = deque()
                    bfs_queue.append((i, j))

                    while len(bfs_queue):
                        top_pos = bfs_queue[0]
                        grid[top_pos[0]][top_pos[1]] = "0" 
                        bfs_queue.popleft()
        
                        dx_dy = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                        for dx, dy in dx_dy: 
                            new_x = top_pos[0] + dx
                            new_y = top_pos[1] + dy
                            if new_x>=0 and new_y>=0 and new_x<m and new_y<n and grid[new_x][new_y] == "1": 
                                bfs_queue.append((new_x, new_y))
                            
        return count