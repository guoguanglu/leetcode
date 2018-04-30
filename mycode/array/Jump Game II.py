class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        level, curlevel_max, nextlevel_max = 1, nums[0], 0
        for i in range(len(nums)):
            if i > curlevel_max:
                level += 1
                curlevel_max = nextlevel_max
            nextlevel = i + nums[i]
            if nextlevel > nextlevel_max:
                nextlevel_max = nextlevel
        return level