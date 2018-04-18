#n-1 makes end bit different from others
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        retstr=''
        while(n>0):
            retstr = chr((n-1)%26+ord("A"))+retstr
            n = (n-1)/26
        return retstr