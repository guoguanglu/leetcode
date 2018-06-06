class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0]<=nums[-1]:
            return nums[0]
        left = 0
        right = len(nums)-1
        min_val = nums[0]
        while left < right:
            mid = (left + right)/2
            if nums[mid]<nums[mid-1] and nums[mid]< nums[mid+1]:
                return nums[mid]
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return nums[mid+1]
            if nums[mid]<nums[0]:
                right = mid
            else:
                left = mid