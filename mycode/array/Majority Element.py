class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for elem in set(nums):
            if nums.count(elem)>len(nums)/2:
                return elem