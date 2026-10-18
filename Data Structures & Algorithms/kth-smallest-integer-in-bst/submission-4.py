# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #in order traversal
        self.inorder = []
        def dfs(root):
            if not root:
                return
            
            #first check for a left
            dfs(root.left)

            #after process the current node and then check right
            self.inorder.append(root.val)

            #Check right side
            dfs(root.right)
        dfs(root)
        return self.inorder[k - 1]
