def subsetSum(l,target):
            mat = [[True if i == 0 else False for i in range(target+1)] for j in range(len(l)+1)]
            for i in range(1,len(l)+1):
                for j in range(1,target+1):
                    if(l[i]>j):
                        mat[i][j] = mat[i-1][j]
                    else:
                        mat[i][j] = mat[i-1][j] or mat[i-1][j-l[i]]
            return mat[-1][-1]