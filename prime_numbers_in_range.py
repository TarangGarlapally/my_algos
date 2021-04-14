#Sieve of Eratosthenes

class Solution:
    def solve(self, n):
        if(n<=1):
            return []
        b = [True for i in range(n+1)]
        b[1] = b[0] = False
        l = []
        for i in range(2,n):
            for j in range(i**2,n+1,i):
                b[j] = False
        for i in range(2,n+1):
            if(b[i] == True):
                l.append(i)
        return l
