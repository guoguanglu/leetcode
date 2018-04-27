# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#my code is that recurse method : individed five conditions :
#1. t==None
#2. t.left==None and t.right==None, for this condition ,we need return t.val
#3. t.left!=None and t.right==None,for this condition ,we need return str(t.val)+'('+self.tree2str(t.left)+')'
#4. t.left ==None and t.right!=None, for this condition,we need return str(t.val)+'()'+'('+self.tree2str(t.right)+')'
#5. t.left != None and t.right != None,for this condition,we need return str(t.val) +'('+ self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')'
class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if t==None:
            return ''
        if t.left==None and t.right==None:
            return str(t.val)
        elif t.left!=None and t.right==None:
            return str(t.val)+'('+self.tree2str(t.left)+')'
        elif t.left ==None and t.right!=None:
            return str(t.val)+'()'+'('+self.tree2str(t.right)+')'
        elif t.left != None and t.right != None:
            return str(t.val) +'('+ self.tree2str(t.left)+')'+'('+self.tree2str(t.right)+')'