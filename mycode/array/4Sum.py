#like 3sum Closest
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        retlist = []
        sortedlist = sorted(nums)
        for i in range(len(nums)-3):
            if sortedlist[i]  > target/4.0:
                break
            if sortedlist[i] == sortedlist[i-1] and i != 0:
                continue
            target2 = target - sortedlist[i]
            for j in range(i+1, len(nums)-2):
                if sortedlist[j]> target2/3.0:
                    break
                if sortedlist[j] == sortedlist[j-1] and j!= i+1:
                    continue
                target3 = target2 - sortedlist[j]
                left = j + 1
                right = len(nums)-1
                if sortedlist[left] > target3/2.0:
                    continue
                if sortedlist[right] < target3/2.0:
                    continue
                while left < right:
                    temp = [sortedlist[i],sortedlist[j],sortedlist[left],sortedlist[right]]
                    if sum(temp) == target:
                        retlist.append(temp)
                        left += 1
                        right -= 1
                        while left < right and sortedlist[left]== sortedlist[left - 1]:
                            left += 1
                        while left < right and sortedlist[right]== sortedlist[right +1]:
                            right -= 1
                    elif sum(temp) > target:
                        right -= 1
                    elif sum(temp) < target:
                        left += 1
        return retlist