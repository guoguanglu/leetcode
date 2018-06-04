#from kleedy
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        temp = []
        stack = []
        heights.append(0)
        for i, each in enumerate(heights):
            cpos = i
            while stack and each < stack[-1][0]:
                h, cpos = stack.pop()
                temp.append(h*(i - cpos))
            stack.append([each, cpos])
        return max(temp) if temp else 0