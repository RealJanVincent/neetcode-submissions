# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        d1 = self.depth(root.left)
        d2 = self.depth(root.right)
        if abs(d1 - d2) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    def depth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            d1 = self.depth(root.left)
            d2 = self.depth(root.right)
            return max(d1, d2) + 1