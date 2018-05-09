class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        pre1, pre2=cost[0], cost[1]
        for elem in cost[2:]:
            temp=pre1
            pre1=pre2
            pre2=min(pre2+elem,temp+elem)
        ret = min(pre1,pre2)
        return ret