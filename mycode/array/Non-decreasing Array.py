class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        tol = 0
        i = 1
        max_inf=1000000
        min_inf=-max_inf
        if len(nums)<=2:
            return True
        nums = [min_inf]+nums+[max_inf]
        while i < len(nums)-1 and tol<2:
            if nums[i]<=nums[i+1]:
                i+=1
            else:
                if nums[i+1]<nums[i-1]:
                    nums[i+1]=nums[i]
                tol+=1
                i+=1
        if tol==2:
            return False
        else:
            return True