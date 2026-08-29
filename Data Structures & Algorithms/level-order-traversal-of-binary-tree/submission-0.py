# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        node_dict = dict()
        node_queue = deque()
        if root:
            node_queue.append((root, 0))

        while len(node_queue):
            top_node, depth = node_queue.popleft()
            if depth in node_dict: 
                node_dict[depth].append(top_node.val)
            else: 
                node_dict[depth] = [top_node.val]

            if top_node.left: 
                node_queue.append((top_node.left, depth+1))
            if top_node.right: 
                node_queue.append((top_node.right, depth+1))
            
        for val in node_dict.values(): 
            res.append(val)
            
        return res

        