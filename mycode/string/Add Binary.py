# bin() can get such as bin(2)="0b10"
#eval() can convert string to int 
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(eval("0b"+a)+eval("0b"+b))[2:]