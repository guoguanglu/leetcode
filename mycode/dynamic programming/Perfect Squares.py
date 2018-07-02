class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # method one dp Time exceed
        #         dp = [0]+[999999]*n
        #         for i in range(n):
        #             for j in range(1,n+1):
        #                 if i+j*j<=n:
        #                     dp[i+j*j] = min(dp[i+j*j],dp[i]+1)

        #                 else:
        #                     break
        #         return dp[-1]
        #       method two Four square sum theorem
        while n % 4 == 0: n /= 4
        if (n % 8 == 7): return 4
        for i in range(n + 1):
            if i * i <= n:
                j = int((n - i * i) ** 0.5)
                if i ** 2 + j ** 2 == n:
                    return (i > 0) + (j > 0)
            else:
                break
        return 3