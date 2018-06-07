class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not len(matrix) or not len(matrix):
            return []
        m = len(matrix)
        n = len(matrix[0])
        res = []
        count=0
        max_count = m*n
        m -= 1
        i, j, di, dj = 0, -1, 0, 1
        while count < max_count:
            for _ in range(n):
                i += di
                j += dj
                res.append(matrix[i][j])
                count += 1
            di, dj = dj, -di
            n -= 1
            m, n = n, m
        return res