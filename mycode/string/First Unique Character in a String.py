#find indexs of character that count==1 in str
#then min(index)
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        index=[]
        strlist=list(s)
        for i in set(strlist):
            if strlist.count(i)==1:
                index.append(strlist.index(i))
        if  len(index):
            return min(index)
        else:
            return -1
