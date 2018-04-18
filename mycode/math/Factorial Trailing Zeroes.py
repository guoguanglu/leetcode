# Number of zeros in the factorial and how many factors in factor 5 are equal
#Z = N/5 + N / (5*5) + N/(5*5*5)..... Until N/(5th power of K) is equal to 0
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while(n/5):
            count += n/5
            n /=5
        return count