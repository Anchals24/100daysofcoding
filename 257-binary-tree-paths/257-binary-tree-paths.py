# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        l = self.binaryTreePaths(root.left) #2-> []
        r = self.binaryTreePaths(root.right) #5-> left ->[], 5-> r->[]
        ans = []
        a = "" #""
        a += str(root.val) 
        if l == [] and r == []:
            ans.append(a)
            return ans
        a += "->" 
        if l == [] and r != []:
            for j in r:
                ans.append(a + j)
            return ans
        if r == [] and l != []:
            for i in l: 
                ans.append(a + i)
            return ans
        for i in l: 
            ans.append(a + i)
        for j in r:
            ans.append(a + j)
        return ans
            
            
            
        #l: left subtree paths from root to leaf ["2->5"]
        #r: right subtree paths from root to leaf ["3"]
        
        """
        ans = [1]
        l = ["2,3,1", "2,4,5"]
        """