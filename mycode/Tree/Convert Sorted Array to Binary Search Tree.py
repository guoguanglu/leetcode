# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not len(nums):
            return 
        mid = (len(nums)+1)/2-1
        tempNode = TreeNode(nums.pop(mid))
        if len(nums):
            leftnums = nums[:mid]
            tempNode.left = self.sortedArrayToBST(leftnums)
            rightnums = nums[mid:]
            tempNode.right = self.sortedArrayToBST(rightnums)
        return tempNode