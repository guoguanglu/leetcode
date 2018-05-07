class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        if len(num)<3:
            return max(num)
        else:
            x=sorted(num)
            return x[-3]