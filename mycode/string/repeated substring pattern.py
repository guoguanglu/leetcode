#method one : try substring from 1 to len(s)/2
#method two : if s in (s+s)[1:-1], true
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #method one
        '''
        temp=''
        for i in range(len(s)/2):
            temp += s[i]
            if temp*(len(s)/(i+1))==s:
                return True
        return False'''
        #method two
        return s in (s+s)[1:-1]