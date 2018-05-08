class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        temp = sum(nums[0:k])
        max_value=temp
        for i,elem in enumerate(nums[k:]):
            temp = temp - nums[i]+elem
            if max_value< temp:
                max_value= temp
        return max_value*1.0/k