#from nirajgoel
#coding
class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid: return

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, self.doDfs(grid, i, j, 1))

        return max_area

    def doDfs(self, grid, i, j, count):
        # convert 1 int 0,which can aviod repeating
        grid[i][j] = 0
        for m, n in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            if (m >= 0 and m < len(grid) and n >= 0 and n < len(grid[0]) and grid[m][n] == 1):
                # 'count' callable arg can add all directions 1 together
                count = 1 + self.doDfs(grid, m, n, count)

        return count
