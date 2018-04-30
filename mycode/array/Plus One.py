class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        n = len(digits)
        for i in range(n):
            num += digits[i]*10**(n-i-1)
        return [int(i) for i in str(num+1)]