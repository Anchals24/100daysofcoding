# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sametree(self, root1, root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        l = self.sametree(root1.left, root2.left)
        r = self.sametree(root1.right, root2.right)
        if (root1.val == root2.val) and l == True and r == True:
            return True
        return False
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None and subRoot == None: 
            return True
        if root == None and subRoot != None:
            return False
        if root != None and subRoot == None:
            return True
        left = self.isSubtree(root.left, subRoot) #(4,4) -> (1,4) -> False
        right = self.isSubtree(root.right, subRoot)
        if root.val == subRoot.val:
            l = self.sametree(root.left, subRoot.left)
            r = self.sametree(root.right, subRoot.right)
            if l == True and r == True:
                return True
        if left == True or right == True:
            return True 
        return False
            
        
        
        
        
        