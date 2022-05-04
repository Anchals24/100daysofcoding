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
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        l = self.isBalanced(root.left)
        r = self.isBalanced(root.right)
        left = self.height(root.left)
        right = self.height(root.right)
        if abs(left-right) <= 1 and l == True and r == True:
            return True
        return False
        