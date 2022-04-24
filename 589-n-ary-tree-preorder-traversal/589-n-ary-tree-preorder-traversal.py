"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children #[3,2,4]
"""

class Solution:
    def helper(self, r, ans):
        if r is None:
            return 
        ans.append(r.val)
        for c in r.children:
            self.helper(c, ans)
            
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        self.helper(root, ans)
        return ans
        
        