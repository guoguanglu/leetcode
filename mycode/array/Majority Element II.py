class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        times = N / 3
        dict_res = {}
        for n in nums:
            if n not in dict_res.keys():
                dict_res.setdefault(n, 1)
            else:
                dict_res[n] += 1
        return [key for (key, value) in dict_res.items() if value > times]
