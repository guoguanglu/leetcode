#missing number = no missing sum - missing sum
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        return size*(size+1)/2-sum(nums)