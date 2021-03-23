class Solution:
    def solve(self, a, b, c):
        l=[]
        def calc(a,b,c,i,j,k):
            nonlocal l
            if(i==len(a) and j==len(b)):
                l.append(True)
                return
            if(k == len(c)):
                return
            x = c[k]
            if( i <len(a) and x == a[i]):
                
                calc(a,b,c,i+1,j,k+1)
            if(j<len(b) and x == b[j]):
                
                calc(a,b,c,i,j+1,k+1)
            l.append(False)
        calc(a,b,c,0,0,0)
        print(l)
        if(True in l):
            return True
        return False
        

