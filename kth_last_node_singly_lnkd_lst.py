# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, k):
        ptr = node
        i=0
        while(i<k):
            ptr = ptr.next
            i+=1
        while(ptr.next!=None):
            ptr = ptr.next
            node = node.next
        return node.val