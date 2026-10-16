# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root):
            if not root:
                return None

            #Both p and q are smaller than root, so the LCA must be in the left subtree
            if root.val > p.val and root.val > q.val:
                return dfs(root.left)

            #Both p and q are larger than root, so the LCA must be in the right subtree
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right)

            #Otherwise p and q split across root (or root equals one of them), so root is the LCA
            else:
                return root

        return dfs(root)

