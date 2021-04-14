# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def solve(self, root):
        node = None
        res = None
        if(root == None):
            return node
        q = deque()
        q.append(root)
        while(q):
            x = q.popleft()
            temp_node = LLNode(x.val)
            if(node == None):
                node = temp_node
                res = node
            else:
                node.next = temp_node
                node = node.next
            if(x.left!=None):
                q.append(x.left)
            if(x.right!=None):
                q.append(x.right)
        return res