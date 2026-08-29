"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.created_nodes = dict()
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None
        else: 
            cp_node = Node(node.val)
            self.created_nodes[node.val] = cp_node
            for nb_node in node.neighbors:
                if nb_node.val in self.created_nodes: 
                    cp_node.neighbors.append(self.created_nodes[nb_node.val])
                else:
                    cp_node.neighbors.append(self.cloneGraph(nb_node))
            return cp_node
        