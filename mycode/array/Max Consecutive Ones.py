class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp=0
        max1=0
        for elem in nums:
            if elem==1:
                temp+=1
            else:
                if max1<temp:
                    max1=temp
                temp=0
        if max1<temp:
            max1=temp
        return max1