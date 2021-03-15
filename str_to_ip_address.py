class Solution:
    def solve(self, ip):
        res = []
        def fun(ip,l):
            if(len(l) == 4 and len(ip) == 0):
                nonlocal res
                res.append(".".join(l))
                return 
            f=0
            
            for i in range(len(ip)):
                l2 = l[:]
                if(len(ip[f:i+1])<4 and int(ip[f:i+1]) <= 255 and len(str(int(ip[f:i+1]))) == len(ip[f:i+1])):
                    l2.append(ip[f:i+1])
                    if(len(l2)<=4):
                        fun(ip[i+1:],l2)
        fun(ip,[])
        return res
            