class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)< 1 or sum(nums)< s:
            return 0
        ret, left, cur_sum= len(nums), 0, 0
        for right, num in enumerate(nums):
            cur_sum += num
            while cur_sum >= s:
                ret, cur_sum, left = min(ret, right - left + 1),cur_sum - nums[left], left + 1
        return ret