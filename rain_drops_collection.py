class Solution:
    def solve(self, nums):
        if(len(nums)<=2):
            return 0
        front = 0
        for i in range(1,len(nums)):
            if(nums[i]<nums[front]):
                break
            front = i
        back = len(nums) - 1
        for i in range(back,front, -1):
            if(nums[i]<nums[back]):
                break
            back = i
        s = 0
        if(nums[front+1:back+1] == []):
            return s
        x = max(nums[front+1:back+1])
        # idx = nums[front+1:].index(x)
        for i in range(front, back):
            if(nums[i] == x):
                x = max(nums[i+1:back+1])
            if(nums[i]<nums[front]):
                if(x>nums[i]):
                    s += min(nums[front],x) - nums[i]
                else:
                    front = i
            else:
                front = i
        return s

                

