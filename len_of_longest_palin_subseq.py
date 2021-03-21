#Reference: https://www.youtube.com/watch?v=_nCsPn7_OgI

#length of longest palindromic subsequence

#above video contains both length and also finding the string

class Solution:
    def solve(self, s):
        if(s == ""):
            return 0
        n = len(s)
        mat = [[0 for i in range(n)] for j in range(n)]
        l = 1
        for d in range(n):
            for i in range(n-d):
                j = i + d
                if(d == 0):
                    mat[i][j] = 1
                    continue
                if(s[i] == s[j]):
                    mat[i][j] = 2 + mat[i+1][j-1]
                else:
                    mat[i][j] = max(mat[i+1][j],mat[i][j-1])
        return mat[0][-1]