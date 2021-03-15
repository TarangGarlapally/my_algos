#Swap subtrees
class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def solve(self, root):
        if root == None or ((root.left == root.right) == None):
            return root
        else:

            #Swap subtrees
            root.left,root.right = root.right,root.left
            if(root.left!=None):
                self.solve(root.left)
            if(root.right!=None):
                self.solve(root.right)
            return root
