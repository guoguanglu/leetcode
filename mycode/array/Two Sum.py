class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numsort=sorted(nums)
        left=0
        right=len(nums)-1
        while left < right:
            if numsort[left]+numsort[right]==target:
                leftindex=nums.index(numsort[left])
                nums[leftindex]='a'
                rightindex=nums.index(numsort[right])
                return [leftindex,rightindex]
            elif numsort[left]+numsort[right]<target:
                left+=1
            else:
                right-=1