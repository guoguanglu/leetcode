#reverse len k,not reverse len k.....
#method one my own code
#method two great code 
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        #method one
        '''
        flag=0
        count=0
        strlist=list(s)
        ret=''
        temp=''
        for elem in strlist:
            temp+=elem
            count +=1
            if count>=k:
                if flag==0:
                    ret += temp[::-1]
                    flag=1
                else:
                    ret += temp
                    flag=0
                count = 0
                temp=''
        if flag==0:
            ret += temp[::-1]
        else:
            ret +=temp
        return ret
        '''
        strlist=list(s)
        for i in range(0,len(strlist),2*k):
            strlist[i:i+k]=strlist[i:i+k][::-1]
        return ''.join(strlist)