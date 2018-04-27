#left and right point compare
#if left!=right,other elements are individed into two parts
#one part removes left and another part removes right
#if two parts are at least one true, then return True
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0,len(s)-1
        while left < right:
            if s[left]!=s[right]:
                one,two=s[left:right],s[left+1:right+1]
                return one==one[::-1] or two==two[::-1]
            left += 1;right -= 1
        return True