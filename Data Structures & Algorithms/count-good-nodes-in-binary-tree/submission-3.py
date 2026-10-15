# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if not root:
                return 0 
            
            currentValue = root.val
            happy = 0
            
            if currentValue >= maxVal:
                #We found a good node
                maxVal = currentValue
                happy = 1
            
    
            return happy + dfs(root.left, maxVal) + dfs(root.right, maxVal)
            

        return dfs(root, root.val)
