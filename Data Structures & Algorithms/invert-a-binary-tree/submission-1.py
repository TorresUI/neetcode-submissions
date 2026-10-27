# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        

        def dfs(root):
            if not root:
                return None
            
            #otherwise get the left sub tree and right subtree then swap and return up
            print(root.val)
            leftRoot = dfs(root.left)
            rightRoot = dfs(root.right)
            root.left = rightRoot
            root.right = leftRoot
            return root
        
        dfs(root)
        return root