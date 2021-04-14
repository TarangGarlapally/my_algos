from collections import deque
class Solution:
    def solve(self, matrix):
        n = len(matrix); m = len(matrix[0])
        vis = [[0 for i in range(m)] for j in range(n)]
        c = 0
        for i in range(n):
            for j in range(m):
                if(vis[i][j]==1):
                    continue
                if(matrix[i][j] == 0):
                    continue
                dx = [0,0,1,-1]
                dy = [1,-1,0,0]
                q = deque()
                q.append([i,j])
                vis[i][j] = 1
                c += 1
                while(q):
                    x = q.popleft()
                    a,b = x[0],x[1]                
                    for k in range(4):
                        if(a+dx[k]<0 or a+dx[k]>=n or b+dy[k]<0 or b+dy[k]>=m or vis[a+dx[k]][b+dy[k]] == 1):
                            continue
                        if(matrix[a+dx[k]][b+dy[k]] == 1):
                            q.append([a+dx[k],b+dy[k]])
                        vis[a+dx[k]][b+dy[k]] = 1

        return c