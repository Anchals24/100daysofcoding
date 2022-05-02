# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        if p == None and q != None:
            return False
        if p != None and q == None:
            return False
        l= self.isSameTree(p.left, q.left)
        r= self.isSameTree(p.right, q.right)
        if (p.val == q.val) and (l == True) and (r==True):
            return True
        return False
        
            
        