class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        nums.sort()
        for elem in nums:
            res += [temp+[elem] for temp in res if temp+[elem] not in res]
        return res