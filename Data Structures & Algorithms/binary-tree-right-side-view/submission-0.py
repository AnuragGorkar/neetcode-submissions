# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root: 
            return res
        else: 
            node_queue = deque()
            node_queue.append(root)

            while len(node_queue): 
                queue_size = len(node_queue) 
                while queue_size>1: 
                    top_node = node_queue.popleft()
                    if top_node.left:
                        node_queue.append(top_node.left) 
                    if top_node.right: 
                        node_queue.append(top_node.right)
                    queue_size-=1
                top_node = node_queue.popleft() 
                res.append(top_node.val)
                if top_node.left:
                    node_queue.append(top_node.left) 
                if top_node.right: 
                    node_queue.append(top_node.right)
            
            return res