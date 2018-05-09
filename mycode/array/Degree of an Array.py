class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #dict={'1':[num,len,last_index]}
        numsdict={}
        for index,elem in enumerate(nums):
            if elem not in numsdict:
                numsdict[elem]=[1,1,index]
            else:
                numsdict[elem][0]+=1
                numsdict[elem][1]+=index-numsdict[elem][2]
                numsdict[elem][2] = index
        value = numsdict.values()
        ret=[0,0,0]
        for elem in value:
            if ret[0]<elem[0]:
                ret=elem
            elif ret[0]==elem[0]:
                if ret[1]>elem[1]:
                    ret=elem
        return ret[1]
