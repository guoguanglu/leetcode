class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        if len(matrix)<2:
            return True
        pre = matrix[0]
        for cur in matrix[1:]:
            if pre[:-1]!=cur[1:]:
                return False
            pre = cur
        return True