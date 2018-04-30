class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        M, N = len(obstacleGrid), len(obstacleGrid[0])
        dp = [1] + [0] * (N-1)
        for i in range(M):
            for j in range(N):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0
                elif j > 0:
                    dp[j] += dp[j-1]
        return dp[N-1]