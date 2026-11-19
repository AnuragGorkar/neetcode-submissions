class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        adj = defaultdict(list)
        for u, v in redEdges:
            adj[u].append((v, 1))
        for u, v in blueEdges:
            adj[u].append((v, 0))

        res = [sys.maxsize] * n

        visited = [[False, False] for _ in range(n)]

        bfs_queue = deque()
        bfs_queue.append((0, 1, 0))
        bfs_queue.append((0, 0, 0))
        visited[0] = [True, True]

        while bfs_queue:
            node, color, distance = bfs_queue.popleft()
            if res[node]>distance:
                res[node] = distance
            for nb_node, nb_edge_color in adj[node]:
                if nb_edge_color != color and not visited[nb_node][nb_edge_color]:
                    visited[nb_node][nb_edge_color] = True
                    bfs_queue.append((nb_node, nb_edge_color, distance+1))

        for i in range(n):
            if res[i] == sys.maxsize:
                res[i] = -1
        return res
        