class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return 0
        maxnum = max(nums)
        maxindex = nums.index(maxnum)
        nums.remove(maxnum)
        secondnum = max(nums)
        if secondnum*2<=maxnum:
            return maxindex
        else:
            return -1