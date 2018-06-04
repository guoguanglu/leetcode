# Definition for a binary tree node.
#from Google
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        temp = postorder.pop()
        node = TreeNode(temp)
        item = inorder.index(temp)
        node.right = self.buildTree(inorder[item+1:], postorder)
        node.left = self.buildTree(inorder[:item], postorder)
        return node