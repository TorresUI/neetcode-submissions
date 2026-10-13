# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lca = None

        def dfs(root):
            if not root:
                return

            if (p.val >= root.val and q.val <= root.val) or (q.val >= root.val and p.val <= root.val ):
                nonlocal lca
                lca = root

            if p.val > root.val and q.val > root.val:
                #Need to check right for lca
                dfs(root.right)
            
            if p.val < root.val and q.val < root.val:
                #Need to check left for lca
                dfs(root.left)
            
        dfs(root)

        return lca