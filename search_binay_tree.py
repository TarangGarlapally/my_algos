# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, val):
        
        
        if(root == None):
            return False
        if(root.val == val):
            return True
        a = self.solve(root.left,val)
        b = self.solve(root.right,val)
        return a or b
