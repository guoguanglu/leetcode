# 9              9                            9*10**0*1
# 99             9 + 90*2                    9*10**0*1+9*10**1*2
# 999            9+90*2+900*3                9*10**0*1+9*10**1*2+9*10**2*3
# we find nth number length range
# then find the determined number
# find the number which bit
class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        ten_power = 0
        bitnum = 1
        temp = 9
        while (n > temp):
            bitnum += 1
            ten_power += 1
            temp += 9 * bitnum * 10 ** ten_power
        n = n - temp+9 * bitnum * 10 ** ten_power
        mod = n%bitnum
        n = n/bitnum
        if mod==0:
            return int(str(10**(bitnum-1)+n-1)[-1])
        else:
            return int(str(10**(bitnum-1)+n)[mod-1])