#we don't convert the inputs to integer
#two parts
#first,compute both numbers the same part
#second,compute long part, individed two parts,carry=1 and carry=0
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        retstr=''
        carry =0
        # add the same part
        for i in range(min(len(num1),len(num2))):
            retstr = chr((ord(num1[-1-i])-ord('0')+ord(num2[-1-i])-ord('0')+carry)%10+ord('0'))+retstr
            carry = (ord(num1[-1-i])-ord('0')+ord(num2[-1-i])-ord('0')+carry)/10
        #add the long part
        #carry=0
        if carry==0:
            if len(num1)>len(num2):
                retstr = num1[:len(num1)-len(num2)]+retstr
                return retstr
            elif len(num1)<len(num2):
                retstr = num2[:len(num2)-len(num1)]+retstr
                return retstr
            else:
                return retstr
        else:
        #carry=1
            if len(num1)>len(num2):
                for i in range(len(num1)-len(num2)):
                    retstr = chr((ord(num1[len(num1)-len(num2)-i-1])-ord('0')+carry)%10+ord('0'))+retstr
                    carry =(ord(num1[len(num1)-len(num2)-i-1])-ord('0')+carry)/10
                    if carry==0:
                        break
                if carry==0:
                    retstr = num1[:len(num1)-len(num2)-i-1]+retstr
                else:
                    retstr = '1'+retstr
                return retstr
            elif len(num1)<len(num2):
                for i in range(len(num2)-len(num1)):
                    retstr = chr((ord(num2[len(num2)-len(num1)-i-1])-ord('0')+carry)%10+ord('0'))+retstr
                    carry =(ord(num2[len(num2)-len(num1)-i-1])-ord('0')+carry)/10
                    if carry==0:
                        break
                if carry==0:
                    retstr = num2[:len(num2)-len(num1)-i-1]+retstr
                else:
                    retstr ='1'+retstr
                return retstr
            else:
                retstr = '1'+retstr
                return retstr