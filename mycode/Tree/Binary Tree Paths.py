# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        retlist = []
        self.getpath(root, retlist)
        return retlist

    def getpath(self, root, retlist, temp=''):
        if not root:
            return
        temp += str(root.val)
        if root.left == root.right == None:
            retlist.append(temp)
        temp += '->'
        if root.left:
            self.getpath(root.left, retlist, temp)
        if root.right:
            self.getpath(root.right, retlist, temp)