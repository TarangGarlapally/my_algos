class Solution:
    def longest_common_subseq(self,a,b):
        mat = [[0 for i in range(len(a)+1)] for j in range(len(b)+1)]
        for i in range(1, len(b)+1):
            for j in range(1,len(a)+1):
                if(b[i-1] == a[j-1]):
                    mat[i][j] = mat[i-1][j-1]+1
                else:
                    mat[i][j] = max(mat[i-1][j],mat[i][j-1])
        return mat[-1][-1]
    def solve(self, a, b):
        #length of shortest common supersequence = len(a) + len(b) - lcs
        return len(a)+len(b) - self.longest_common_subseq(a,b)
        