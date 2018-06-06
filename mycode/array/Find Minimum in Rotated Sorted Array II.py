class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left, right, ret = 0, len(nums)-1, nums[0]
        while left <= right:
            while left < right and nums[left]==nums[left+1]:
                left +=1
            while left < right and nums[right] == nums[right-1]:
                right -=1
            mid = (left + right)/2
            if nums[mid]>=nums[0]:
                left = mid+1
            else:
                right = mid-1
                ret = min(ret, nums[mid])
        return ret