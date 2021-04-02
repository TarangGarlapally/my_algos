# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        res = True
        def calcHeight(root,h):
            if(root == None):
                return h+0

            a = calcHeight(root.left, h)
            b = calcHeight(root.right,h)
            h += max(a, b)
            if(abs(a - b)>1):
                nonlocal res
                res = False
            return h

        calcHeight(root,1)
        return res
        # if(root.left == None and root.right == None):
        #     return res
        
        # check(root)