"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return 
        Stack = deque()
        Stack.append(root)
        ans = []
        while len(Stack) > 0:
            temp = Stack.pop()
            ans.append(temp.val)
            for c in range(len(temp.children)-1, -1, -1):
                if temp.children[c] != None:
                    Stack.append( temp.children[c])
        return ans
            