class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        def hasCycle(u, v):
            # Check if path exists from u to v (before adding edge)
            visited = set()
            stack = [u]
            while stack:
                node = stack.pop()
                if node == v:
                    return True
                visited.add(node)
                for neighbor in graph[node]:
                    if neighbor not in visited:
                        stack.append(neighbor)
            return False
        
        for u, v in edges:
            if hasCycle(u, v):  # Adding this edge creates cycle
                return [u, v]
            graph[u].append(v)
            graph[v].append(u)