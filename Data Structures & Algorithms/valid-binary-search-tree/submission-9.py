# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #the middle node is bouded by negative infinity and positive infinity.
        #All decendents to the left of the root are bounded by negative infinity and the root.
        #all decendents to the right of the root are bounded by positive infinity.

        #Decendents to the right are lower bounded by their parent 

        def dfs(left, curr, right):
            if not curr:
                return True
            
            if curr.val >= right or curr.val <= left:
                return False
            
            #otherwise keep exploring and return the and of both branches
            #when going to the left the left bound is the same as the parent and the right bound becomes the parent
            #when going to the right the right bound is the same as the parent and the left bound becomes the parent.
            return dfs(left, curr.left, curr.val) and dfs(curr.val, curr.right, right)
        
        return dfs(float('-inf'), root, float('inf'))
