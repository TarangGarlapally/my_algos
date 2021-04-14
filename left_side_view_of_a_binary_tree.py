# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        d = {}
        def exploreAndAdd(root, depth):
            if(root == None):
                return
            if(depth not in d):
                d[depth] = root.val
            exploreAndAdd(root.left, depth+1)
            exploreAndAdd(root.right, depth+1)
        
        exploreAndAdd(root, 0)
        d = list(sorted(d.items(), key = lambda x: x[0]))
        return [x[1] for x in d]
    