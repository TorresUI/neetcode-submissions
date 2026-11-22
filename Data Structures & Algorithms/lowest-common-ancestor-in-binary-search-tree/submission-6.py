# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(curr):
            if curr.val == p.val:
                return curr
            if curr.val == q.val:
                return curr

            #otherwise we have a number that we need to explore. 
            #If the numbers are in difference branches we found the LCS

            if (p.val > curr.val and q.val < curr.val) or (p.val < curr.val and q.val > curr.val):
                return curr
            
            #if the numbers are in the right or left branch we need to explore
            if p.val > curr.val and q.val > curr.val:
                return dfs(curr.right)
            elif p.val < curr.val and q.val < curr.val:
                return dfs(curr.left)
        
        return dfs(root)