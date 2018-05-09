class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        ret = []
        cur = 'A'
        temp = []
        count = 0
        for i, elem in enumerate(S):
            if cur == elem:
                count += 1
            else:
                cur = elem
                if count >= 3:
                    temp.append(i - 1)
                    ret.append(temp)
                temp = [i]
                count = 1
        if count >= 3:
            temp.append(i)
            ret.append(temp)
        return ret
