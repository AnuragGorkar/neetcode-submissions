# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -sys.maxsize
        def maxPathSumFromNode(node):
            nonlocal res
            if not node: 
                return 0
            else: 
                max_left_sum = maxPathSumFromNode(node.left)
                max_right_sum = maxPathSumFromNode(node.right)
                res = max(res, node.val, node.val+max_left_sum, node.val+max_right_sum, node.val+max_left_sum+max_right_sum)
                return max(node.val, node.val+max_left_sum, node.val+max_right_sum)
        maxPathSumFromNode(root)
        return res