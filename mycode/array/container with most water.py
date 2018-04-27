#method:start from the maxwidth,then gradually decrease width
#left and right two points ,which small,which move
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxwater = 0
        i , j = 0 , len(height) -1
        while i < j:
            maxwater = max(maxwater, (j-i)*min(height[i],height[j]))
            if height[i]<=height[j]:
                i += 1
            else:
                j -= 1
        return maxwater