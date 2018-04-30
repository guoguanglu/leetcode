class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        retlist=[[]]
        for elem in nums:
            retlist += [[elem]+temp for temp in retlist]
        return retlist