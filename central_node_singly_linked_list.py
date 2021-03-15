# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        ptr = node
        while(ptr != None and ptr.next!=None):
            ptr = ptr.next
            ptr = ptr.next
            node = node.next
        return node.val