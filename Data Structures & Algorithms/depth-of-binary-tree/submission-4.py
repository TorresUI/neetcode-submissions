# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root):
            if not root:
                #We have reached a null 
                return 0
            
            #we have a valid node. compute the max depth of left + right
            depthLeft = dfs(root.left)
            depthRight = dfs(root.right)

            maxDepth = max(depthLeft, depthRight)
            return 1 + maxDepth
        
        return dfs(root)