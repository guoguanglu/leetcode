class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret=0
        if len(prices)<2:
            return ret
        temp = prices[0]
        for elem in prices[1:]:
            if temp < elem:
                ret+=elem-temp
            temp=elem
        return ret