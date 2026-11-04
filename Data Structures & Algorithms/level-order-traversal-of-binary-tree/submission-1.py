# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        else:
            l = self.levelOrder(root.left)
            r = self.levelOrder(root.right)
            shorter, longer = l, r
            if len(r) < len(l):
                shorter, longer = r, l
            res = [None for i in range(len(longer) + 1)]
            res[0] = [root.val]
            for i in range(len(shorter)):
                res[i + 1] = l[i] + r[i]

            for i in range(len(shorter), len(longer)):
                res[i + 1] = longer[i]
            return res

        