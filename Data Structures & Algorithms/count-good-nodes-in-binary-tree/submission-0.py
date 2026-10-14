# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0
        def dfs(root, maxNum):
            if not root:
                return
            
            if root.val >= maxNum:
                nonlocal res
                maxNum = root.val
                res += 1
            
            dfs(root.right, maxNum)
            dfs(root.left, maxNum)
        
        dfs(root, root.val)
        return res
                
            