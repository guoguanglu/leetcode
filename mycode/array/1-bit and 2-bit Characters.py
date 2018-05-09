class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i=0
        bits[-1]=1
        while i < len(bits):
            if bits[i]:
                i+=2
            else:
                i+=1
        if i==len(bits):
            return False
        else:
            return True