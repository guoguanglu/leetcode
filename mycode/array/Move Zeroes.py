class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zerosnum=nums.count(0)
        for i in range(zerosnum):
            nums.remove(0)
            nums.append(0)