class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r = len(grid)
        c = len(grid[0])
        cur = [x[0] for x in grid]
        for i in range(1, r):
            cur[i] += cur[i - 1]  # initial cur
        for j in range(1, c):
            cur[0] += grid[0][j]
            for i in range(1, r):
                cur[i] = min(cur[i], cur[i - 1]) + grid[i][j]
        return cur[r - 1]
