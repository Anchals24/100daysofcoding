# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root):
        if root is None:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ldia = self.diameterOfBinaryTree(root.left)
        rdia = self.diameterOfBinaryTree(root.right)
        passrootl = self.height(root.left) - 1
        passrootr = self.height(root.right) - 1
        passroot = passrootl + passrootr + 2
        notroot = max(ldia, rdia)
        return max(passroot, notroot)
       
        
        