# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bal, d = self.balDepth(root)
        return bal
    
    def balDepth(self, root: Optional[TreeNode]) -> (bool, int):
        if root == None:
            return (True, 0)
        b1, d1 = self.balDepth(root.left)
        b2, d2 = self.balDepth(root.right)
        if b1 and b2: 
            return (abs(d1 - d2) <= 1, max(d1, d2) + 1)
        else:
            return (False, -1)