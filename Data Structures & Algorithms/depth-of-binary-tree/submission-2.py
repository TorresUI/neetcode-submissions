# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(root):
            if not root:
                return 0
            
            #Otherwise we want to compute the depth and then return the height of the tree      
            currHeight = 1 + max(dfs(root.left), dfs(root.right))
            self.res = max(self.res, currHeight)

            return currHeight
        
        dfs(root)
        return self.res
