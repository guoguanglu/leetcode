class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        elif len(nums)==0:
            return 0
        a = nums[:-1]
        b = nums[1:]
        print a,b
        return max(self.not_circle_rob(a),self.not_circle_rob(b))
    def not_circle_rob(self,nums):
        pre = 0
        cur = 0
        for i in nums:
            pre, cur = cur, max(pre+i, cur)
        return cur