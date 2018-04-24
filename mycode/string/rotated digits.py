#one step: remove '3','4','7'
#two step: must include one of ['2','5'.'6','9']
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count=0
        for i in range(1, N + 1):
            if '3' in str(i) or '4' in str(i)or'7'in str(i):
                continue
            for each in ['2','5','6','9']:
                if each in str(i):
                    count+=1
                    break
        return count
