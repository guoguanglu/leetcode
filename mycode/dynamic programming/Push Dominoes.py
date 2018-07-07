class Solution(object):
    def pushDominoes(self, d):
        d = 'L' + d + 'R'
        res = []
        i = 0
        for j in range(1, len(d)):
            if d[j] == '.': continue
            middle = j - i - 1
            if i: res.append(d[i])
            if d[i] == d[j]: res.append(d[i] * middle)
            elif d[i] == 'L' and d[j] == 'R': res.append('.' * middle)
            else: res.append('R' * (middle / 2) + '.' * (middle % 2) + 'L' * (middle / 2))
            i = j
        return ''.join(res)