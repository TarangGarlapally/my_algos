from collections import defaultdict
class Solution:
    def solve(self, nums):

        d = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            d[nums[i]] += 1
            ans += d[nums[i]]
        return ans

        