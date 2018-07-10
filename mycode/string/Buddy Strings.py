class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A)!= len(B):
            return False
        if A == B:
            if len(set(A))!=len(A):
                return True
            else:
                return False
        else:
            diff = [(a, b) for a, b in zip(A, B) if a!=b]
            return len(diff)==2 and diff[0] == diff[1][::-1]