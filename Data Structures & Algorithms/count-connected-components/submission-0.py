class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for a, b in edges: 
            adj[a].append(b)
            adj[b].append(a)
        
        visited = [False for _ in range(n)]

        cc = 0

        while True:
            discovered = False
            for i in range(n):
                if not visited[i]:
                    discovered = True
                    cc += 1

                    bfs_queue = deque()
                    bfs_queue.append(i)

                    while len(bfs_queue):
                        node = bfs_queue.popleft()
                        visited[node] = True
                        for nb in adj[node]:
                            if not visited[nb]:
                                bfs_queue.append(nb)

            if not discovered:
                break

        return cc