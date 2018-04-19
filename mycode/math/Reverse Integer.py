#use the conversion between string type and int type
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret=0
        if x >= 0:
            ret = int(str(x)[::-1])
        if x<0:
            ret = -int(str(x)[::-1][0:-1])
        if ret <= 2**31-1 and ret>=-2**31:
            return ret
        else:
            return 0