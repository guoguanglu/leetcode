#from lee215 great code
#example "0110001111"=[1,2,3,4] = min(1,2)+min(2,3)+min(3,4)=6
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = map(len, s.replace("01","0 1").replace("10","1 0").split())
        return sum(min(a,b) for a,b in zip(s,s[1:]))