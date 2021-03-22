# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#gives values of tree as seen from above, root will be up and every node below the top nodes will be hidden

class Solution:
    def solve(self, root):
        d = {}
        def rankNodes(root,rank, level):
            if(root == None):
                return
            nonlocal d
            if(root.left != None):
                if(rank-1 not in d or d[rank-1][1] > level+1):
                    d[rank-1] = [root.left.val,level+1]
                rankNodes(root.left,rank-1,level+1)
            if(root.right != None):
                if(rank+1 not in d or d[rank+1][1] > level+1):
                    d[rank+1] = [root.right.val,level+1]
                rankNodes(root.right,rank+1,level+1)
                

        d[0] = [root.val,1]
        rankNodes(root,0,1)
        d = sorted(list(d.items()), key = lambda x: x[0])
        res = [x[1][0] for x in d]
        return res