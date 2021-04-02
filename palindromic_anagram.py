from collections import Counter
class Solution:
    def solve(self, s):
        # d = {}
        # for x in s:
        #     if(x in d):
        #         d[x] += 1
        #     else:
        #         d[x] = 1
        # vals = d.values()
        # ABOVE IS ALSO CORRECT BUT TAKES MORE TIME THAN BELOW COUNTER FUNC
        vals = collections.Counter(s)
        
        f = 0
        for x in vals.values():
            if(x%2 == 1 and f==0):
                f = 1
            elif(x%2 == 1):
                return False
        return True