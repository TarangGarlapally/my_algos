class Solution:
    def solve(self, matrix):
        if( matrix == [] or matrix == [[]]):
            return []
        if(len(matrix) == 1):
            return matrix[0]
        l = []
        i = 0
        j = 0
        c = 0; f = 0
        if(True):
            while(len(l)<len(matrix[0])*len(matrix)):

                l.append(matrix[i][j])
                
                if(len(l) == len(matrix[0])*len(matrix)):
                    break
                lim = len(matrix[0])
                if(f == 0 and j < lim - 1 - c):
                    j += 1
                elif(f == 1 and j > 0 + c):
                    j -= 1
                    
                elif(f == 0 and i < len(matrix) - 1 - c):
                    i += 1
                    if(i == len(matrix)-1 - c):
                        f = 1
                elif(f == 1 and i > 0 + c):
                    i -= 1
                    if(i == 0+c):
                        
                        i = 1+c; j = 1+c
                        c += 1; f=0
                else:
                    c += 1
                    f = 0
                    l.pop()
                    i = 0 + c
                    j = 0 + c

        return l

            