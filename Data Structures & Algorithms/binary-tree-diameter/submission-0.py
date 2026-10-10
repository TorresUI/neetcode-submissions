# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            if not root:
                return 0

            depthLeft = dfs(root.left)
            depthRight = dfs(root.right)
            nonlocal res
            res = max(res, depthLeft + depthRight)

            return 1 + max(depthLeft, depthRight)
        
        dfs(root)

        return res