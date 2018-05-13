class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left=0
        right = len(nums)-1
        sortnums = sorted(nums)
        while(left<len(nums)):
            if sortnums[left]==nums[left]:
                left+=1
            else:
                break
        while right>left:
            if sortnums[right]==nums[right]:
                right-=1
            else:
                break
        return right-left+1