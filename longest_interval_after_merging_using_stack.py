
class Solution:
    def solve(self, intervals):
        intervals.sort(key = lambda x: x[0])
        stack = []
        stack.append(intervals[0])
 
        i = 0
        for i in range(len(intervals)):
            if(intervals[i][0]<=stack[-1][1]) and stack[-1][1]>intervals[i][1]:
                pass
            elif(stack[-1][1]>=intervals[i][0]):
                temp = [stack[-1][0],intervals[i][1]]
                stack.pop()
                stack.append(temp)
            else:
                stack.append(intervals[i])
            i+=1


        r = 0
        for x in stack:
            if(x[1]-x[0] +1>r):
                r = x[1]-x[0] +1
        return r
                

