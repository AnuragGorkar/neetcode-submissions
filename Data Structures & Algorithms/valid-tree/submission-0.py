from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = [False for _ in range(n)]
        adj = defaultdict(list)

        for n1, n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(node, par_node):
            if visited[node]:
                return False
            else: 
                visited[node] = True
                for nb in adj[node]:
                    if par_node != nb:
                        if not dfs(nb, node):
                            return False
                return True

        if not dfs(0, -1):
            return False

        for v in visited:
            if not v:
                return False

        return True