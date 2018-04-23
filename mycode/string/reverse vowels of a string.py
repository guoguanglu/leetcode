#two pointers:left and right
#left pointer vowel converts with right pointer vowel each other
#until left>=right
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret=list(s)
        vowel="aeiouAEIOU"
        left=0
        right=len(s)-1
        while(left<right):
            if ret[left] in vowel:
                temp = ret[left]
                while left<right:
                    if ret[right] in vowel:
                        ret[left]= ret[right]
                        ret[right]=temp
                        right -=1
                        left +=1
                        break
                    else:
                        right-=1
            else:
                left+=1
        return ''.join(ret)