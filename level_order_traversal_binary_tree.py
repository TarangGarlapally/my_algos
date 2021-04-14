# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def solve(self, root):
        if(root == None):
            return []
        q = deque()
        q.append(root)
        l = []
        while(q):
            x = q.popleft()
            l.append(x.val)
            if(x.left != None):
                q.append(x.left)
            if(x.right != None):
                q.append(x.right)
        return l