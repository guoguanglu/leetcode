class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<2:
            return len(nums)
        pre=nums[0]
        maxnum=1
        temp=1
        for elem in nums[1:]:
            if elem > pre:
                temp +=1
            else:
                if maxnum<temp:
                    maxnum=temp
                temp=1
            pre=elem
        if maxnum<temp:
            maxnum = temp
        return maxnum