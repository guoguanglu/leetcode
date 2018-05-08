class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        point=0
        nums = [0]*(len(nums)-len(set(nums)))+list(set(nums))
        cur=1
        for elem in nums:
            if elem == cur:
                cur+=1
            elif elem > cur:
                nums[point:point+elem-cur]=range(cur,elem)
                point += elem -cur
                cur += elem-cur+1
        return nums[:point]+range(cur,len(nums)+1)