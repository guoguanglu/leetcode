#one step: let len(A)>=len(B),
#then C=A*int(ceil(len(B)*1.0/len(A)))
#two step: if B not in C+A,then B isn't repeated string of A

from math import ceil
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        C = A*int(ceil(len(B)*1.0/len(A)))
        if B not in C+A:
            return -1
        elif B in C:#probable B=C
            return int(ceil(len(B)*1.0/len(A)))
        return int(ceil(len(B)*1.0/len(A)))+1