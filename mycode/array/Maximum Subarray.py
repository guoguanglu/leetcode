class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dynamic planning
        if len(nums)==1:
            return nums[0]
        dp = nums[0]
        maxnum=nums[0]
        for elem in nums[1:]:
            if dp<0:
                dp=elem
            else:
                dp+=elem
            if maxnum<dp:
                maxnum = dp
        return maxnum