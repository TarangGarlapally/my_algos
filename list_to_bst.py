# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, nums):
        def construct(nums):
            if(len(nums) == 0):
                return
            root = Tree(nums[len(nums)//2])
            root.left = construct(nums[:len(nums)//2])
            root.right = construct(nums[len(nums)//2+1:])
            return root
        return construct(nums)