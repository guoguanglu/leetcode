class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = pos_max = neg_max = nums[0]
        for elem in nums[1:]:
            pos_max ,neg_max= max(elem, elem*pos_max, elem*neg_max), min(elem, elem * pos_max, elem * neg_max)
            max_value = max(pos_max, max_value)
        return max_value