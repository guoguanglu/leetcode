#if not empty, output = min(m)*min(n)
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        #method1
        if ops==[]:
            return m*n
        ops1=[x[0] for x in ops]
        ops2=[x[1] for x in ops]
        return min(ops1)*min(ops2)
        '''
        #method2 expand  min()
        for elem in ops:
            if elem[0]<m:
                m = elem[0]
            if elem[1]<n:
                n=elem[1]
        return m*n
        '''

