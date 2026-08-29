# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: 
            return ""
        else:
            preorder_string = ""
            def preorderTrav(node, index): 
                if not node: 
                    return ""
                else:
                    res = str(node.val) + "=" + str(index)
                    if(node.left):
                        res += " "+preorderTrav(node.left, index+1)
                    if(node.right):
                        res += " "+preorderTrav(node.right, index+2)
                    return res
            preorder_string = preorderTrav(root, 1)

            inorder_string = ""
            def inorderTrav(node, index): 
                if not node: 
                    return ""
                else: 
                    res = ""
                    if(node.left):
                        if res: 
                            res += " "
                        res += inorderTrav(node.left, index+1)
                    if res: 
                        res += " "
                    res += str(node.val) + "=" + str(index)
                    if(node.right):
                        if res: 
                            res += " "
                        res += inorderTrav(node.right, index+2)
                    return res
            inorder_string = inorderTrav(root, 1)
            return preorder_string + "_" + inorder_string

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not len(data): 
            return None
        else:
            preorder = data.split("_")[0].split(" ")
            inorder = data.split("_")[1].split(" ")

            def buildTree(preorder, inorder): 
                if len(preorder)==0: 
                    return None
                else: 
                    node = TreeNode(int(preorder[0].split("=")[0]))
                    index = inorder.index(preorder[0])
                    node.left = buildTree(preorder[1:index+1], inorder[0:index])
                    node.right = buildTree(preorder[index+1:], inorder[index+1:])
                    return node

            return buildTree(preorder, inorder)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))