#first,initial primes=[1]*n and primes[0:2]=0
#according to i*i,i*(i+1),i*(i+2).... all numbers are not primes
#then primes[i*i:n:i]=0
#importance
#if primes[j]=0 and i<j,then primes[i*i:n:i] includes primes[j*j:n:j],we don't need to compute
#because i*x=j, j*x'=i*(x*x')
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        primes=[1]*n
        primes[0:2]=[0,0]
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i]=[0]*len(primes[i*i:n:i])
        return sum(primes)