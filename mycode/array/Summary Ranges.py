class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums)<1:
            return []
        res = []
        N = len(nums)
        nums.append(999999)
        i = 0
        while i < N:
            flag=0
            temp = str(nums[i])
            while nums[i+1] - nums[i]==1:
                i+=1
                flag=1
            if flag==1:
                temp = temp + '->' + str(nums[i])
            res.append(temp)
            i +=1
        return res