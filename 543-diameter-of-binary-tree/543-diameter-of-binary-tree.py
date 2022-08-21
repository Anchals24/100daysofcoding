# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def heighbt(self, root):
        if root is None:
            return 0
        return 1 + max(self.heighbt(root.left), self.heighbt(root.right))
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)
        maxdia = max(ldia, rdia)
        lheight = self.heighbt(root.left)
        rheight = self.heighbt(root.right)
        return max((lheight + rheight), maxdia)
        
        
        #root: height of left + height of right
        
        
        