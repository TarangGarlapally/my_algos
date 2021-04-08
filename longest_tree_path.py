# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        path = 0
        def calcPath(root):
            if(root == None):
                return
            a = calcPath(root.left) if root.left!=None else 0
            b = calcPath(root.right) if root.right!=None else 0
            t_path = 1 + a + b
            nonlocal path
            if(t_path>path):
                path = t_path
            return max(a,b) + 1
        
        calcPath(root)
        return path