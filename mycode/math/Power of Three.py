#don't use recurse , use loga(b)=log10(a)/log10(b),
#and modf()function gets decimal part , if decimal part !=0, false
from math import*
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            return modf(log10(n)/log10(3))[0]==0