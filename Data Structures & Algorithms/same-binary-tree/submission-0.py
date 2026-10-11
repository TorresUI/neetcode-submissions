# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(root1, root2):
            if root1 and root2 and root1.val != root2.val:
                return False
            
            if not root1 and not root2:
                return True

            if not root1 and root2 or root1 and not root2:
                return False
            
            #Need to do DFS on left and right

            leftBool = dfs(root1.left, root2.left)
            rightBool = dfs(root1.right, root2.right)

            return leftBool and rightBool
        
        return dfs(p, q)