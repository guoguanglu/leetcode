# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        cur_quenen = [root]
        ret=[]
        while cur_quenen:
            next_depth_quenen = []
            cur_val = []
            for node in cur_quenen:
                cur_val.append(node.val)
                if node.left:
                    next_depth_quenen.append(node.left)
                if node.right:
                    next_depth_quenen.append(node.right)
            cur_quenen=next_depth_quenen
            ret = [cur_val] + ret
        return ret