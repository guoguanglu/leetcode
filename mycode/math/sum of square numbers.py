#a**2+b**2=c,then b max= int(c**0.5),
#we can left and right method to find the result
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 0
        b = int(c**0.5)
        while(a <= b):
            if a**2+b**2 == c:
                return True
            elif a**2+b**2 > c:
                b -= 1
            else:
                a += 1
        return False