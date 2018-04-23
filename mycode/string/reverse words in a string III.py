class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        wordlist = s.split()
        for i,word in enumerate(wordlist):
            wordlist[i] = word[::-1]
        return ' '.join(wordlist)