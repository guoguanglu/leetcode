#formule ABCD=A*26**3+B*26**2+C*26**1+D*26**0
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1]
        ret=0
        for i,each in enumerate(s):
            ret += (ord(each)-ord('A')+1)*26**i
        return ret