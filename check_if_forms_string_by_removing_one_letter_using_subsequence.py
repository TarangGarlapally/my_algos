class Solution:
    def solve(self, s0, s1):
        if(len(s0) != len(s1) + 1):
            return False
        i = 0
        f = 0
        l = 0
        for j in range(len(s1)):
            if(s0[i]!=s1[j]):
                if(f==1):
                    return False
                f = 1
                i += 1
            if(s0[i] == s1[j]):
                l += 1
            i+=1
        if(l == len(s1)):
            return True
        return False