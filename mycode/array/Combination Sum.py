class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(sorted(candidates), target, [], 0)
        return self.res

    def helper(self, c, target, combo, index):
        exceed = False
        for i in range(index, len(c)):
            if exceed:
                break
            combo.append(c[i])
            if target - c[i] > 0:
                self.helper(c, target - c[i], combo, i)
            elif target - c[i] == 0:
                self.res.append(list(combo))
                exceed = True
            else:
                exceed = True
            combo.pop()
        return