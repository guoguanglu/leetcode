class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i,each in enumerate(nums+[0]):
            if each < target:
                continue
            else:
                break
        return i