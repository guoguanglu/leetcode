class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return False
        r = len(matrix)
        c = len(matrix[0])
        row_left=0
        row_right= r-1
        temp = row_left
        if matrix[0][0]>target:
            return False
        if matrix[r-1][c-1]<target:
            return False
        if matrix[r-1][0] > target:
            while(1):
                if matrix[temp][0]== target or matrix[row_right][0]==target:
                    return True
                elif matrix[temp][0]>target:
                    row_right = temp
                elif matrix[temp][0]<target:
                    row_left = temp
                if temp == (row_left+row_right)/2:
                    break
                else:
                    temp = (row_left+row_right)/2
        else:
            temp = r-1
        col_left=0
        col_right=c-1
        temp2 = col_left
        while(1):
            if matrix[temp][temp2]==target or matrix[temp][col_right]==target:
                return True
            elif matrix[temp][temp2]>target:
                col_right = temp2
            elif matrix[temp][temp2]<target:
                col_left = temp2
            if temp2 == (col_left+col_right)/2:
                return False
            else:
                temp2 = (col_left+col_right)/2