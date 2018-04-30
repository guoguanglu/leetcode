class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r = len(matrix)
        c = len(matrix[0])
        r_zero=[0]*r
        c_zero=[0]*c
        for i in range(r):
            if (matrix[i]+[0]).index(0)!=c:
                r_zero[i] = 1
            for j in range(c):
                if matrix[i][j] ==0:
                    c_zero[j]=1
        for i, elem in enumerate(r_zero):
            if elem==1:
                matrix[i]=[0]*c
        for i, elem in enumerate(c_zero):
            if elem==1:
                for row in range(r):
                    matrix[row][i] = 0