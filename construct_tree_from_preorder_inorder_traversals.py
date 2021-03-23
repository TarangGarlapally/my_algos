# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, preorder, inorder):
        if(preorder == []):
            return None
        root = None
        def construct(inorder):
            idx = -1
            nonlocal preorder
            try:
                idx = inorder.index(preorder[0])
            except:
                return
            root = Tree(preorder[0])

            preorder.pop(0)
            root.left = construct(inorder[:idx])
            root.right = construct(inorder[idx+1:])
            return root

          
                
        root  = construct(inorder)
        return root

        