# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        K = k
        def dfs(node): 
            nonlocal K
            if not node:
                return None
            else: 
                left = dfs(node.left) 
                if left: return left
                K-=1
                if not K:
                    return node
                right = dfs(node.right) 
                if right: return right
                return None
        return dfs(root).val
        