class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        m = len(nums)
        n = len(nums[0])
        ret=[]
        temp=[]
        if m*n!=r*c:
            return nums
        for i in range(m):
            for j in range(n):
                temp.append(nums[i][j])
                if len(temp)==c:
                    ret.append(temp)
                    temp=[]
        return ret