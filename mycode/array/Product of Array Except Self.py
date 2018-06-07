class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        temp = 1
        for i in range(len(nums)):
            res.append(temp)
            temp *= nums[i]

        temp = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * temp
            temp *= nums[i]
        return res

