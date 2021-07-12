
class Solution:
    def solve(self, matrix):
        m = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        
        m[0][0] = matrix[0][0]
       


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if(i==0 and j == 0):
                    continue
                if(i == 0):
                    m[i][j] = m[i][j-1] + matrix[i][j]
                elif(j == 0):
                    m[i][j] = m[i-1][j] + matrix[i][j]
                else:
                    m[i][j] = max(m[i][j-1], m[i-1][j])+matrix[i][j]
        return m[-1][-1]
                