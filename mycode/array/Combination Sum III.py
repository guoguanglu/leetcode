class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper([], 1, k, n)
        return self.res

    def helper(self, s, index, k, n):
        if k == 0:
            if sum(s) == n:
                self.res.append(list(s))
            return
        for i in range(index, 10):
            s.append(i)
            if sum(s) <= n:
                self.helper(s, i + 1, k - 1, n)
                s.pop()
            else:
                s.pop()
                break
        return