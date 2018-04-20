#use sum to find duplicated number and missing number
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        missing = (1+len(nums))*len(nums)/2-sum(set(nums))
        dupnum =sum(nums)-sum(set(nums))
        return [dupnum, missing]