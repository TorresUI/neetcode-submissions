# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(root, root2):

            if root and root2 and root.val != root2.val:
                return False
            
            if not root and not root2:
                return True

            if not root and root2 or root and not root2:
                return False
            
            #Need to do DFS on left and right

            leftBool = isSameTree(root.left, root2.left)
            rightBool = isSameTree(root.right, root2.right)

            return leftBool and rightBool

        if not root and subRoot or root and not subRoot:
            return False

        if root and subRoot and root.val == subRoot.val and isSameTree(root, subRoot):
            return True
        else:

            subTreeLeft = self.isSubtree(root.left, subRoot)
            subTreeRight = self.isSubtree(root.right, subRoot)
        
        return subTreeLeft or subTreeRight

            
