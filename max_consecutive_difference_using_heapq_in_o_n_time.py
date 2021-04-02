import heapq
class Solution:
    def solve(self, nums):
        n = len(nums)
        heapq.heapify(nums)
        res = 0
        t = heapq.heappop(nums)
        for i in range(n-1):
            newt = heapq.heappop(nums)
            if(newt - t > res):
                res = newt - t
            t = newt
        return res
        