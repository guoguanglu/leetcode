class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(M)
        n = len(M[0])
        average = 0
        count = 0
        ret = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    average += M[i - 1][j]
                    count += 1
                    if j - 1 >= 0:
                        average += M[i - 1][j - 1]
                        count += 1
                    if j + 1 < n:
                        average += M[i - 1][j + 1]
                        count += 1
                average += M[i][j]
                count += 1
                if j - 1 >= 0:
                    average += M[i][j - 1]
                    count += 1
                if j + 1 < n:
                    average += M[i][j + 1]
                    count += 1
                if i + 1 < m:
                    average += M[i + 1][j]
                    count += 1
                    if j - 1 >= 0:
                        average += M[i + 1][j - 1]
                        count += 1
                    if j + 1 < n:
                        average += M[i + 1][j + 1]
                        count += 1
                ret[i][j] = average / count
                average = 0;
                count = 0
        return ret


