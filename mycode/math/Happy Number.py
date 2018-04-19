#mem saves history number, if n in mem ,false
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        mem =[]
        while(n!=1):
            mem.append(n)
            n = sum([int(x)**2 for x in str(n)])
            if n in mem:
                return False
        return True