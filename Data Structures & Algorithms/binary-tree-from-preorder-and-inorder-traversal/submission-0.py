# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getIndex(self, array, target):
        for i in range(len(array)): 
            if array[i] == target: 
                return i
        return -1 

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder)==0:
            return None
        else: 
            node = TreeNode(preorder[0])
            
            inorder_index = self.getIndex(inorder, preorder[0])

            left_preorder = preorder[1:inorder_index+1]
            left_inorder = inorder[0:inorder_index]
            node.left = self.buildTree(left_preorder, left_inorder)

            right_preorder = preorder[inorder_index+1:]
            right_inorder = inorder[inorder_index+1:]
            node.right = self.buildTree(right_preorder, right_inorder)

            return node
        