# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def ismirror(self, root1, root2):
        if root1 == None and root2 == None: 
            return True
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        l = self.ismirror(root1.left, root2.right) #(3,4) -> (lNone, lNone) -> True
        r = self.ismirror(root1.right, root2.left) #(3,4) -> (rnone, rnone) -> True 
        if (root1.val == root2.val)  and (l == True) and (r == True):
            return True
        return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 
        return self.ismirror(root.left, root.right) #(2,2)
        
        
        
        
        
        
        
        
        
        """
        elif root1.left == None and root2.right != None:
            left = False
        elif root1.left != None and root2.right == None:
            left = False
            
            
            
            
        left = False
        if root1.left != None and root2.right != None:
            if root1.left.val == root2.right.val:
                left = True
        elif root1.left == None and root2.right == None:
            left = True
            
        right = False
        if root2.left != None and root1.right != None:
            if root2.left.val == root1.right.val:
                right = True
        elif root2.left == None and root1.right == None:
            right = True
            
            
            """
        
        