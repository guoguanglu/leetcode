class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        A = [[0]*n for _ in range(n)]
        i, j , id, jd = 0, 0 , 0 ,1
        for k in range(n*n):
            A[i][j] = k+1
            if A[(i+id)%n][(j+jd)%n]:
                id, jd = jd, -id
            i += id
            j += jd
        return A