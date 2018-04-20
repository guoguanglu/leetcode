#according to the formula :
#n*(n+1)/2=coins,n=int((-1+sqrt(1+8*coins))/2)
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int((-1+(1+8*n)**0.5)/2)