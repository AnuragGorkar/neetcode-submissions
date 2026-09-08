# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        count = 0

        def recurCount(node, max_till_now):
            nonlocal count
            if not node:
                return
            if node.val >= max_till_now:
                count += 1
            max_till_now = max(max_till_now, node.val)
            recurCount(node.left, max_till_now)
            recurCount(node.right, max_till_now)
            
        recurCount(root, -1*float('inf'))


        return count
        