#following the question meaning
class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = []
        for i in range(left,right+1):
            flag=0
            strnum = str(i)
            mod =0
            for elem in strnum:
                if elem=='0':
                    flag=1
                    break
                else:
                    if i%int(elem)!=0:
                        flag=1
                        break
            if flag==0:
                ret.append(i)
        return ret