class Solution:
    def solve(self, nums):
        if(len(nums) == 1):
            return []
        l = []
        for i in range(len(nums)):
            if(i==0 and nums[i+1]<nums[i]):
                l.append(i)
                continue
            if(i == len(nums)-1 and nums[i]>nums[i-1]):
                l.append(i)
                continue
            if(nums[i]>nums[i-1] and nums[i]>nums[i+1]):
                l.append(i)
        return l 

