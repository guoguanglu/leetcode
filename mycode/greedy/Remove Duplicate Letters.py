class Solution(object):
    def removeDuplicateLetters(self, s):
        rindex = {c: i for i, c in enumerate(s)}
        ret = ''
        for i, c in enumerate(s):
            if c not in ret:
                while c < ret[-1:] and i < rindex[ret[-1]]:
                    ret = ret[:-1]
                ret += c
        return ret