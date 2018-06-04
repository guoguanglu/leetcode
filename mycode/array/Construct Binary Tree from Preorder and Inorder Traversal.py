class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(preorder)==0 or len(inorder)==0:
            return None
        temp = preorder.pop(0)
        node = TreeNode(temp)
        inorder_index = inorder.index(temp)
        node.left = self.buildTree(preorder, inorder[:inorder_index])
        node.right = self.buildTree(preorder, inorder[inorder_index+1:])
        return node