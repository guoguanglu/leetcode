# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        #realize back ret by list  
        ret = [True]
        self.treeDepth(root, ret)
        return ret[0]
    def treeDepth(self, root, ret):
        if not root:
            return 0
        left_depth = self.treeDepth(root.left,ret)
        right_depth = self.treeDepth(root.right,ret)
        if left_depth - right_depth>1 or left_depth-right_depth<-1:
            ret[0] = False
        if left_depth>right_depth:
            return left_depth+1
        else:
            return right_depth+1