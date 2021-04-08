class Solution:
    def solve(self, nums):
        skip = 0
        not_skip = 0
        for i in range(len(nums)):
            if(i == 0):
                s = 0
                not_skip = nums[i]
                continue
            if_skip_i = not_skip
            if_not_skip_i = min(skip,not_skip) + nums[i]
            skip = if_skip_i
            not_skip = if_not_skip_i
        return min(skip,not_skip)
