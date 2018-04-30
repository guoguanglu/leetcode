#the method two steps:
#first we need sort target
#second we fix one, others are left point and right point respect
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sortedlist = sorted(nums)
        ans = sortedlist[0]+sortedlist[1]+sortedlist[2]
        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                sumtemp = sortedlist[i] +sortedlist[j] +sortedlist[k]
                if abs(target - ans) > abs(target - sumtemp):
                    ans = sumtemp
                if sumtemp == target:
                    break
                elif sumtemp > target:
                    k -= 1
                elif sumtemp < target:
                    j += 1
            if sumtemp == target:
                break
        return ans