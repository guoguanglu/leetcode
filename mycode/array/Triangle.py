class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        temp = triangle[-1]
        for elem in triangle[:-1][::-1]:
            for i, num in enumerate(elem):
                temp[i] = num + min(temp[i], temp[i+1])
        return temp[0]