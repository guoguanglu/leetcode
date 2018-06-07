class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0
        for cur_index, value in enumerate(nums):
            nums[cur_index] = 2
            if value < 2 :
                nums[j] = 1
                j += 1
            if value == 0:
                nums[i] = 0
                i += 1