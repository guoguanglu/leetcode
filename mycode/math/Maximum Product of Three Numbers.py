#three numbers product the max = max(max1*max2*max3,max1*min1*min2)
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return max([nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1]])