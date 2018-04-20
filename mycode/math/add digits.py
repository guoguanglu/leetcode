#input 0,1,2,3,4...
#output 0,1,2,3,4,5,6,7,8,9,1,2,3...
#n%9=1,2,3,4,5,6,7,8,0,responding output 1,2,3,4,5,6,7,8,0
#so (n-1)%9=0,1,2,3,4,5,6,7,8 responding output 1,2,3,4,5,6,7,8,9
#so 1+(n-1)%9 = output
#ret = x if x==0 x=0 else x=1+(num-1)%9
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num==0:
            return 0
        return 1+(num-1)%9