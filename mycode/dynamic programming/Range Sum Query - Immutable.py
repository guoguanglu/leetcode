class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.val = nums
        for i in range(1,len(nums)):
            self.val[i] += self.val[i-1]
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.val[j]
        else:
            return self.val[j]-self.val[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)