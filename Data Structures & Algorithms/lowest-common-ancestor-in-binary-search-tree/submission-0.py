# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not node:
            return None
        elif node.val==p.val or node.val==q.val:
            return node
        else: 
            left = self.lowestCommonAncestor(node.left, p, q)
            right = self.lowestCommonAncestor(node.right, p, q)
            if (left and right) or ((left or right) and (node.val == p.val or node.val == q.val)):
                return node
            elif left: 
                return left
            return right
        
        