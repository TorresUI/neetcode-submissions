# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root, left, right):
            if not root:
                return True
            
            #we need to iterate to the left and pass the bounds
            #upper bound will be the current node value 
            #lower bound will be inherited by the parent 

            #check if current node is breaking the bound
            if root.val <= left or root.val >= right:
                return False

            left = dfs(root.left, left, root.val)
            right = dfs(root.right, root.val, right)

            return left and right
        
        return dfs(root, float("-inf"), float("inf"))
