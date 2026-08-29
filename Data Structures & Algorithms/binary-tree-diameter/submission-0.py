# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root): 
            nonlocal res 
            if not root: 
                return 0
            else: 
                l_depth = dfs(root.left)
                r_depth = dfs(root.right)   
                res = max(res, l_depth + r_depth)
                return max(l_depth, r_depth) + 1
        dfs(root)
        return res
        