# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.isMirror(root.left,root.right)
    def isMirror(self,root_left,root_right):
        if root_left==root_right==None:
            return True
        if (root_left and not root_right)or(not root_left and root_right):
            return False
        if root_left.val==root_right.val:
            return self.isMirror(root_left.left,root_right.right) and self.isMirror(root_left.right,root_right.left)
        else:
            return False