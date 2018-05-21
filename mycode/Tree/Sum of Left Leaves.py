# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        retsum = self.sumleftleave_helper(root,0)
        return retsum
    def sumleftleave_helper(self,root,direction):
        if not root:
            return 0
        if not root.left and not root.right and direction:
            return root.val
        retsum = self.sumleftleave_helper(root.left,1) + self.sumleftleave_helper(root.right,0)
        return retsum