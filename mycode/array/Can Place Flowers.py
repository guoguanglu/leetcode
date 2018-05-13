class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        #in order to form the same structure,let flowerbed = [0]+flowerbed+[0]
        #only flowerbed[i-1] and flowerbed[i],flowerbed[i+1] all are zer0,
        #if flowerbed[i]==1, i jump two steps
        #if flowerbed[i]==0, flowerbed[i+1]==1,i jump two steps
        #if flowerbed[i]==0, flowerbed[i-1]=1 and flowerbed[i+1]=0,i jump one step
        maxplant=0
        flowerbed=[0]+flowerbed+[0]
        i=1
        while i<len(flowerbed)-1:
            if flowerbed[i]:
                i+=2
            else:
                if flowerbed[i-1]+flowerbed[i+1]==0:
                    maxplant+=1
                    i+=2
                elif flowerbed[i+1]==1:
                    i+=2
                else:
                    i+=1
        return maxplant>=n