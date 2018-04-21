# the meaning of the question:
#The idea is to output the string 1 when n=1;
# when n=2, count the number of values in the last string,
#  because the previous string has 1 1, so the output 11; n = 3,
# because the last time The character is 11, there are two 1's,
# so the output 21; n = 4, because the last string is 21,
# there is a 2 and 1 1, so the output 1211
# example
#if n-1 : 112233441122
#then n : 212223242122
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        retstr =str(1)
        i=1
        while i<n:
            cur_num = retstr[0]
            num=0
            temp=''
            for elem in retstr:
                if elem == cur_num:
                    num +=1
                else:
                    temp+=str(num)+str(cur_num)
                    num=1
                    cur_num=elem
            temp+=str(num)+str(cur_num)
            retstr=temp
            i+=1
        return retstr