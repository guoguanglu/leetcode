#the so-called number m is a factor of another number n, meaning that n
# can be divisible by m, that is, n %m==0. According to the definition of
# ugly numbers, ugly numbers can only be divisible by 2,3,and 5.Thata is
#to say, if a number is divisible by 5, it is divided by 5.If we finally get
#1, then this number is ugly, otherwise it is not.
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while(num%2==0<num):
            num=num/2
        while(num%3==0<num):
            num=num/3
        while(num%5==0<num):
            num=num/5
        if num==1:
            return True
        else:
            return False