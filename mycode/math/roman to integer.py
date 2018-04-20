# two methods , the same principle
#from left to right ,if left >=right,then ret+=left
#if left < right, then ret+= right -left
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #method 1
        ret =0
        seve_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'0':0}
        s=s+'0'
        i=0
        while(1):
            if s[i] =='0':
                return ret
            elif seve_dict[s[i]]>=seve_dict[s[i+1]]:
                ret +=seve_dict[s[i]]
                i +=1
            else:
                ret += seve_dict[s[i+1]]-seve_dict[s[i]]
                i+=2
        '''
        #method2
        ret =0
        seve_dict = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        i=0
        while(i<len(s)-1):
            if seve_dict[s[i]]>=seve_dict[s[i+1]]:
                ret +=seve_dict[s[i]]
                i +=1
            else:
                ret += seve_dict[s[i+1]]-seve_dict[s[i]]
                i+=2
        if i==len(s):
            return ret
        else:
            ret+=seve_dict[s[-1]]
            return ret
            '''