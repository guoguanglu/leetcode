# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        '''
        p1, q1 = [], []
        self.pretraversing(p,p1)
        self.pretraversing(q,q1)
        return p1==q1
    def pretraversing(self,p,ret):
        if p==None:
            ret.append('null')
            return
        ret.append(p.val)
        self.pretraversing(p.left,ret)
        self.pretraversing(p.right,ret)
        '''
        if p==q==None:
            return True
        if p and q and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
            return True
        else:
            return False