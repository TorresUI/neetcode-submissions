# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(root1, root2):
            if not root1 and not root2:
                return True
            
            if (not root1 and root2) or (root1 and not root2) or (root1.val != root2.val):
                return False
            return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)



        #if both are null return true
        if not root and not subRoot:
            return True
        #if one of them is null but not the other return false
        if (not root and subRoot) or (root and not subRoot):
            return False

        #first find matching root and then calculate if it is the same tree.
        if isSameTree(root, subRoot):
            return True
        
        #Otherwise we need to find the root
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


            