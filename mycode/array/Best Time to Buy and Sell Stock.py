class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #dynamic planning
        if len(prices)<2:
            return 0
        ret=0
        curmin=prices[0]
        for i in range(1,len(prices)):
            ret =max(ret,prices[i]- curmin)
            curmin=min(curmin,prices[i])
        return ret 