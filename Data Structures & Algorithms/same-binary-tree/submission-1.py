# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            #base case both NULL
            if not root1 and not root2:
                return True
            
            if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
                return False
            
            return dfs(root1.left, root2.left) and dfs(root1.right, root2.right)
        
        return dfs(p, q)

