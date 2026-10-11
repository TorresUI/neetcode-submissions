# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return [True, 0]
            
            isBalancedLeft, heightLeft = dfs(root.left)
            isBalancedRight, heightRight = dfs(root.right)
            height = 1 + max(heightLeft, heightRight)
            isBalanced = isBalancedLeft and isBalancedRight and abs(heightLeft - heightRight) <= 1

            return [isBalanced, height]
        
        return dfs(root)[0]