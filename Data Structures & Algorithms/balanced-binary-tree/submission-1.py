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
                #Null base case. Its balanced.
                return [True, 0]

            balancedLeft, heightLeft = dfs(root.left)
            balancedRight, heightRight = dfs(root.right)


            isBalanced = balancedLeft and balancedRight and (abs(heightLeft - heightRight) <= 1)

            return [isBalanced, 1 + max(heightLeft, heightRight)]
        
        return dfs(root)[0]




        #We want to check at every step if it is balanced and return the sum of all balanced. so if balanced its true and we want to return the and union of all balanced checks

        #At each step we want to check the height of left and right as well as if all previous subtrees were balanced. if yes then the given root is balanced.

