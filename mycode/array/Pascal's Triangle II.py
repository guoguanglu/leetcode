class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        ret = [1]
        for i in range(rowIndex):
            ret = [x + y for x, y in zip([0] + ret, ret + [0])]
        return ret
