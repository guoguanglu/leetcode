class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [0,0]+nums
        for i in range(2,n+2):
            if dp[i-1]> dp[i]+dp[i-2]:
                dp[i]=dp[i-1]
            else:
                dp[i]+=dp[i-2]
        return dp[n+1]

    # class Solution(object):
    #     def rob(self, nums):
    #         """
    #         :type nums: List[int]
    #         :rtype: int
    #         """
    #         pre, cur = 0, 0
    #         for n in nums:
    #             pre, cur = cur, max(pre + n, cur)
    #         return cur