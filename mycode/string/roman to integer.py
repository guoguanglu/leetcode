# we add '0' at the end of s
#because we can use the same structure to compute
#if s[i]>=s[i+1],then ret+=s[i],or ret += s[i+1]-s[i]
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
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