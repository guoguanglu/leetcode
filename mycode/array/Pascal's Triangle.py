class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows==0:
            return []
        elif numRows == 1:
            return [[1]]
        ret=[[1]]
        temp=[1]
        for i in range(1,numRows):
            temp=[x+y for x,y in zip([0]+temp,temp+[0])]
            ret.append(temp)
        return ret