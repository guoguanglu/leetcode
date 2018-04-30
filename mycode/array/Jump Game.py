class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        if nums[0] ==0:
            return False
        curlevel_max, nextlevel_max=0, 0
        for i in range(len(nums)):
            if i > curlevel_max:
                if curlevel_max == nextlevel_max:
                    return False
                curlevel_max = nextlevel_max
            nextlevel = i + nums[i]
            if nextlevel > nextlevel_max:
                nextlevel_max = nextlevel
        return True