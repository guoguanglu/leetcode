class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if len(matrix):
            r, c = len(matrix), len(matrix[0])
            self.val = matrix
            for i in range(r):
                for j in range(1, c):
                    self.val[i][j] += self.val[i][j - 1]
        else:
            self.val = 0

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        ret_sum = 0
        if self.val == 0:
            return 0
        for r in range(row1, row2 + 1):
            if col1 == 0:
                ret_sum += self.val[r][col2]
            else:
                ret_sum += self.val[r][col2] - self.val[r][col1 - 1]
        return ret_sum



        # Your NumMatrix object will be instantiated and called as such:
        # obj = NumMatrix(matrix)
        # param_1 = obj.sumRegion(row1,col1,row2,col2)