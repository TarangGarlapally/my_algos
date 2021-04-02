# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        n = 1
        head = node
        prev = None
        while(node!= None and node.next != None):
            node.val, node.next.val = node.next.val, node.val
            node = node.next.next
        return head


