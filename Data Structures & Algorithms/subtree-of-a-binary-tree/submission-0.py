# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, t1, t2):
        if not t1 and not t2:
            return True
        elif (not t1 and t2) or (not t2 and t1):
            return False
        else:
            l = self.isSameTree(t1.left, t2.left)
            r = self.isSameTree(t1.right, t2.right)
            return t1.val == t2.val and l and r

    # def dfs(self, root, subroot, found):
    #     if found:
    #         return True
    #     elif not root and subroot:
    #         return False
    #     else:
    #         l = self.dfs(root.left, subroot, found)
    #         if l:
    #             return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root and not subRoot) or (not subRoot and root):
            return True
        elif not root and subRoot:
            return False
        else:
            l = self.isSubtree(root.left, subRoot)
            r = self.isSubtree(root.right, subRoot)
            if l or r:
                return True
            else:
                return self.isSameTree(root, subRoot)