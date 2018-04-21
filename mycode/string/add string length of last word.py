#two method
#one way: use str.split()
#two way: start from the end position
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        '''
        method1 : use str.split() function
        list = s.split()
        if len(list)==0:
            return 0
        else:
            return len(list[-1])
        '''
        ret = 0
        length = len(s)-1
        while(length>=0 and s[length]==' ' ):
            length -= 1
        while(length>=0 and s[length] !=' '):
            ret += 1
            length -=1
        return ret