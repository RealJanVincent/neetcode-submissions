# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestPath(self, root: Optional[TreeNode]):
        # (n - longest path of a tree, m - longest path that finishes in the root)
        if root == None or (root.left == None and root.right == None):
            return (0, 0)
        l = self.longestPath(root.left)
        r = self.longestPath(root.right)
        addition = 2
        if root.left == None or root.right == None:
            addition = 1
        longestInTree = max(l[0], r[0], addition + l[1] + r[1])
        longestInRoot = max(l[1] + 1 if root.left != None else 0, r[1] + 1 if root.right != None else 0)
        return (longestInTree, longestInRoot)
 
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = self.longestPath(root)
        return d[0]