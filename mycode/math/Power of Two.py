# we can use (n&(n-1)) binary bit operator
#example 4 : 100&011==0,True
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        """
        #my code
        if n<=0:
            return False
        while n%2==0:
            n=n/2
        if n==1:
            return True
        else:
            return False
        """
        #great code
        return n > 0 and (n & (n-1)) == 0