# filter(str.isalnum,str(s)),we can only keep numbers and alphabet
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        news=filter(str.isalnum,str(s)).lower()
        return news==news[::-1]