# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        #we want to recursively traverse down the tree. Find the point where p and q diverge left and right and that will be the lowest common ancestor.
        #if they are both to the left traverse left
        #if they are both to the right traverse right
        #if we reach null ? <--- should never reach this state.

        def dfs(currNode, left, right):
            if (currNode.val >= p.val and currNode.val <= q.val) or (currNode.val <= p.val and currNode.val >= q.val) or currNode.val == p.val or currNode.val == q.val:
                return currNode
            
            #otherwise we need to go either left or right
            if currNode.val > p.val and currNode.val > q.val:
                #curr node is greater than both check left
                return dfs(currNode.left, left, currNode.val)
            
            if currNode.val < p.val and currNode.val < q.val:
                return dfs(currNode.right, currNode.val, right)
        
        return dfs(root, float('-inf'), float('inf'))