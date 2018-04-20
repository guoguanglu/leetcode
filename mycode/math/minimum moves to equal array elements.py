#Incrementing all but one is equivalent to decrementing that one
#great idea from StefanPochmann
#then count = sum(nums) - len(nums)*min(nums)
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums)-len(nums)*min(nums)