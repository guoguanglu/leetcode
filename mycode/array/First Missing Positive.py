#one step: sort
#two step: compare
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        i = 1
        for elem in nums:
            if elem < i:
                continue
            elif elem == i:
                i += 1
            elif elem > i :
                return i
        return i