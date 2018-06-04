class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        i = 0
        for elem in nums:
            if i <2 or elem > nums[i-2]:
                nums[i] = n
                i +=1
        return i
        """
        cur_point = 0
        point = 0
        count = 0
        if len(nums)==0:
            return 0
        oldnum = nums[0]
        while cur_point<len(nums):
            if oldnum == nums[cur_point]:
                count +=1
                if count <3:
                    nums[point] = nums[cur_point]
                    point += 1
            else:
                count = 1
                oldnum = nums[cur_point]
                nums[point] = nums[cur_point]
                point +=1
            cur_point+=1
        return point