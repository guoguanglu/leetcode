class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        right=sum(nums)
        for i in range(len(nums)):
            if i==0:
                left=0
            else:
                left += nums[i-1]
            right -= nums[i]
            if left==right:
                return i
        return -1