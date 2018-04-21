#brute compute, reverse all conditions
#S=|a||b|sin(a,b)/2=|a x b|/2=|x1*y2-y1*x2|/2
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        ret = 0
        for i in range(len(points) - 2):
            for j in range(i + 1, len(points) - 1):
                for k in range(j + 1, len(points)):
                    vector_AB = [points[i][0] - points[j][0], points[i][1] - points[j][1]]
                    vector_AC = [points[i][0] - points[k][0], points[i][1] - points[k][1]]
                    temp = abs(vector_AB[0] * vector_AC[1] - vector_AB[1] * vector_AC[0]) * 1.0 / 2
                    if temp > ret:
                        ret = temp
        return ret
