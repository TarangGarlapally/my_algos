# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        def explore(root):
            if(root == None):
                return
            f = 0
            if(root.left == None and root.right!=None):
                f = 1                    
                root = root.right
            elif(root.left!=None and root.right==None):
                f = 1
                root = root.left
            if(f == 1):
                root = explore(root)
            elif(f == 0):
                root.left = explore(root.left)
                root.right = explore(root.right)
            return root
        root = explore(root)
        return root