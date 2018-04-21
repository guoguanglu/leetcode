# attention : first, I find min(strs),which can avoid the included running error
#example ,["aa",'a'],mini_lenstr must = 'a'
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ret=""
        if len(strs)==0:
            return ret
        elif len(strs)==1:
            return strs[0]
        min_lenstr= min(strs)
        strs.remove(min_lenstr)
        for num,i in enumerate(min_lenstr):
            temp = [i!=elem[num] for elem in strs]
            if sum(temp)==0:
                ret += i
            else:
                break
        return ret