class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        for elem in set(nums):
            if nums.count(elem)>1:
                index=-100000
                for i in range(0,nums.count(elem)):
                    if nums.index(elem)-index<=k:
                        return True
                    else:
                        index=nums.index(elem)
                        nums[index]='a'
        return False