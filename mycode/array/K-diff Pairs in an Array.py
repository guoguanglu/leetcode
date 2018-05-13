class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        point1=0
        point2=1
        ret=0
        if k<0 or len(nums)<2 or nums[len(nums)-1]-nums[0]<k:
            return ret
        while point2<len(nums):
            if point1<point2:
                if nums[point2]-nums[point1]<k:
                    while point2<len(nums)-1 and nums[point2]==nums[point2+1]:
                        point2+=1
                    point2+=1
                elif nums[point2]-nums[point1]==k:
                    ret+=1
                    while point2<len(nums)-1and nums[point2]==nums[point2+1]:
                        point2+=1
                    point2+=1
                    while point2<len(nums)-1 and point1<point2 and nums[point1]==nums[point1+1]:
                        point1+=1
                    point1+=1
                elif  nums[point2]-nums[point1]>k:
                    while point2< len(nums)-1 and point1 < point2 and nums[point1]==nums[point1+1]:
                        point1+=1
                    point1+=1
            else:
                point2+=1
        return ret